# Required by Cloud Function/Run
import functions_framework

# Common Imports
from google.cloud import bigquery
from google.cloud.bigquery.table import Table
from google.cloud import logging

# Common Imports - Optional
from datetime import datetime
import os
import json
import time

from synergia_mysql_client.mysql_connector import MySqlConnector
from synergia_alloydb_client.alloydb_connector import AlloyDbConnector
from synergia_utils.utils import *

from models import UuidMetaData
from golden_gate import GoldenGate, GoldenGateRow

FUNCTION_NAME = os.environ.get("FUNCTION_NAME", "finance-ent-ext")
INSERT_TO_BIGQUERY_CHUNK_SIZE = int(os.environ.get("INSERT_TO_BIGQUERY_CHUNK_SIZE","10000"))
MYSQL_DETAILES_SECRET_KEY = os.environ.get("MYSQL_DETAILES_SECRET_KEY", "projects/205429398886/secrets/mysql_connection_details/versions")
ALLOYDB_SECRET_KEY = os.environ.get('ALLOYDB_SECRET_KEY',"projects/205429398886/secrets/alloy_db_connection_details/versions")

####### init params
appLogName = os.environ.get("APPLOGSNAME", "processapp") 
alloydb_connector = AlloyDbConnector(connection_details_secret_name=ALLOYDB_SECRET_KEY)
mysql_client = MySqlConnector(process_name=FUNCTION_NAME, connection_details_secret_name=MYSQL_DETAILES_SECRET_KEY, pool_size=5)
my_conf = mysql_client.get_config()
print (my_conf)
process_id = my_conf['id']
ds = 'ds_sttsow_devices'
text_for_nlp_table = f'{ds}.text_for_nlp'
target_bq_table = my_conf['target_bq_table'] 
text_for_nlp_alloy_table = f'text_for_nlp'


# Optional in workbench
project_id = 'prj-sttsow-dev' # <Developer>
location = 'me-west1' # <Developer>

bigquery_client = bigquery.Client()

def get_text_from_alloy(uuid_metadata: UuidMetaData) -> list[str]:
    get_text_query = f"""
                        SELECT ARRAY_AGG(text) as text FROM(
                            SELECT json_array_elements_text(full_document_text->'text') as text
                            FROM {text_for_nlp_alloy_table}
                         WHERE uuid = {uuid_metadata.uuid}) as t;
                         """
    rows = alloydb_connector.execute_query(get_text_query)
    for row in rows:
        if isinstance(row['text'], list):
            text_without_quotes = list(map(lambda x: x.strip('"'), row['text']))
            return text_without_quotes
        return []

def split_list_to_chunks(lst, chunk_size):
    if len(lst) <= chunk_size:
        return [lst]
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

def insert_rows_to_bigquery_table(table: Table, rows_2_insert):
    errors = bigquery_client.insert_rows(table, rows_2_insert)  
    if errors == []:
        print(f"New {len(rows_2_insert)} rows have been added to {table}.")
    else: 
        raise Exception("Encountered errors while inserting rows: {}".format(errors))

def get_rows_2_insert(uuid_metadata: UuidMetaData):
    rows_2_insert = []
    for finance_object in uuid_metadata.finance_objects:
        row = {
            "uuid": uuid_metadata.uuid,
            "device_name": uuid_metadata.device_name,
            "original_uri": uuid_metadata.original_uri,
            "exact_match_word": finance_object.exact_match_word,
            "match_group": finance_object.match_group,
            "match_type": finance_object.match_type
        }
        rows_2_insert.append(row)
    return rows_2_insert

def write_result_to_bq(uuid_metadata: UuidMetaData):
    table_ref = bigquery_client.dataset(ds).table(target_bq_table)
    table: Table = bigquery_client.get_table(table_ref)
    rows_2_insert = get_rows_2_insert(uuid_metadata)
    if(rows_2_insert):
        if(len(rows_2_insert) > INSERT_TO_BIGQUERY_CHUNK_SIZE):
            print(f"Starting to insert {len(rows_2_insert)} rows into {target_bq_table} by chunks")
            splited_rows_2_insert = split_list_to_chunks(rows_2_insert, INSERT_TO_BIGQUERY_CHUNK_SIZE)
            for chunk in splited_rows_2_insert:
                insert_rows_to_bigquery_table(table, chunk)
        else:
            insert_rows_to_bigquery_table(table, rows_2_insert)
    else:
        print(f"No new rows to insert to {target_bq_table}")

def convert_pubsub_to_uuidMetaData(pubsub_message: dict):
    if pubsub_message.get('uuid') and pubsub_message.get('device_name') and \
        pubsub_message.get('original_uri') and pubsub_message.get('function_name'):
        message = UuidMetaData(
                    uuid = pubsub_message['uuid'],
                    md5_hash = pubsub_message['md5_hash'],
                    device_name = pubsub_message['device_name'],
                    original_uri = pubsub_message['original_uri'],
                    function_name = pubsub_message['function_name']
                    )
        return message
    else:
        msg = f"invalid Pub/Sub message {pubsub_message}"
        raise Exception(msg)

# Triggered by a pub sub message
@functions_framework.cloud_event
def finance_ent_ext(cloud_event):
    print(f"Starting function {FUNCTION_NAME}")
    golden_gate_client = GoldenGate()
    try:
        pubsub_message: dict = parse_pubsub_cloud_event(cloud_event)
        uuid_metadata: UuidMetaData = convert_pubsub_to_uuidMetaData(pubsub_message)
        mysql_client.insert_to_file_process_log(uuid_metadata.uuid, uuid_metadata.md5_hash, uuid_metadata.device_name, uuid_metadata.original_uri,'inProcess')
        text: list[str] = get_text_from_alloy(uuid_metadata)
        finance_objects: list[GoldenGateRow] = golden_gate_client.run_on_list(text)
        if finance_objects:
            uuid_metadata.finance_objects = finance_objects
            write_result_to_bq(uuid_metadata)
        else:
            print(f"No financial objects found in text for uuid {uuid_metadata.uuid}")
        mysql_client.update_file_process(process_id,uuid_metadata.uuid, 'done')
    except Exception as ex:
        print(f"Got exception {ex}, update status to error in process log")
        mysql_client.update_file_process(process_id, uuid_metadata.uuid, 'done')
    except Exception as ex:
        print("Got exception {ex}, update status to error in process log")
        mysql_client.update_file_process(process_id, uuid_metadata.uuid, 'error', str(ex))