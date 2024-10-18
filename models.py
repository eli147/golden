from typing import Optional
from pydantic import BaseModel
from golden_gate import GoldenGateRow

class UuidMetaData(BaseModel):
    uuid: int
    md5_hash: str
    device_name: int
    original_uri: str
    function_name: str
    finance_objects : list = []
