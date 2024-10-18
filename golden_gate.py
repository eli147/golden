import os
import sys
import re
import datetime
import base58
import bech32
import eth_utils
import monero
import bitcoincash.cashaddr
from schwifty import IBAN

from constants import *


class GoldenGateRow:
    match_type = None
    match_group = None
    exact_match_word = None
 
    def __init__(self, match_type, match_group, exact_match_word):
        self.match_type = match_type
        self.match_group = match_group
        self.exact_match_word = exact_match_word


class GoldenGate:

    uuid = None
    device_name = None

    regexp_map = None
    characters_map = None
    alpha_map = None

    data = set()
    iban_data = []
    credircard_data = []
    ethereum_data = []
    
    test_success = 0
    count_total = 0
    test_goal = 23
    save_chunk_size = 10000
    html_cleanr = re.compile(r'<.*?>|<.*?\.\.\.')
    mnemonic_lengths = [12, 24]
    black_list_words = ['TelegramIPhoneBackupFiles','FacebookFilesIos','http','.mp4','.MP4','.jpg','.pdf','filename','tiktok','marketplace']
    special_chars_list = ['\\n', '|', ';', ',', '"', '<', '>', '=', '?', ':', '-', ' ', '\\', '/', '#', '%', '@', '&', '(', ')', '_', '.',
               '{', '}', '[', ']']
    credit_card_chars = [' ', ':', '|', '\t', '\r', '\rn', '\n']
    goldengate_table_fields = ['analyze_dt', 'match_group', 'match_type', 'exact_match_word', 'gen_match_phrase', 'context_words_list', 'schema_name', 'table_name', 'extra_info']
    fields_to_process = ['title_content', 'body_content']
    identifiers = [
        CryptoCoinWordMatchType.MNEMONIC_PHRASE,
        CryptoCoinWordMatchType.BITCOIN,
        CryptoCoinWordMatchType.ETHEREUM,
        CryptoCoinWordMatchType.TRON,
        CryptoCoinWordMatchType.IBAN,
        CryptoCoinWordMatchType.MONERO,
        CryptoCoinWordMatchType.ZCASH_Z,
        CryptoCoinWordMatchType.ZCASH_T,
        CryptoCoinWordMatchType.LITECOIN,
        CryptoCoinWordMatchType.RIPPLE,
        CryptoCoinWordMatchType.BITCOIN_CASH,
        CryptoCoinWordMatchType.XPUB,
        CryptoCoinWordMatchType.WIF,
        CryptoCoinWordMatchType.CONTAINER,
        CryptoCoinWordMatchType.CREDIT_CARD
    ]


    def __init__(self):
        self.init_attributes()


    def init_attributes(self):
        characters = {
            "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20,
            "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31,
            "W": 32, "X": 33, "Y": 34, "Z": 35,
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
        }

        self.characters_map = { ord(k): str(v) for k, v in characters.items() }

        self.alpha_map = {
            'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20, 'K': 21, 'L': 23, 'M': 24,
            'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
        }

        self.regexp_map = {}
        self.regexp_map[CryptoCoinWordMatchType.MNEMONIC_PHRASE] = RawTextAnalyzerConsts.Mnemonic
        self.regexp_map[CryptoCoinWordMatchType.BITCOIN] = RawTextAnalyzerConsts.BitcoinAddressCurrent
        self.regexp_map[CryptoCoinWordMatchType.ETHEREUM] = RawTextAnalyzerConsts.EthereumAddress
        self.regexp_map[CryptoCoinWordMatchType.TRON] = RawTextAnalyzerConsts.Tron
        self.regexp_map[CryptoCoinWordMatchType.IBAN] = RawTextAnalyzerConsts.Iban
        self.regexp_map[CryptoCoinWordMatchType.MONERO] = RawTextAnalyzerConsts.MoneroAddress
        self.regexp_map[CryptoCoinWordMatchType.ZCASH_Z] = RawTextAnalyzerConsts.ZcashZAddress
        self.regexp_map[CryptoCoinWordMatchType.ZCASH_T] = RawTextAnalyzerConsts.ZcashTAddress
        self.regexp_map[CryptoCoinWordMatchType.LITECOIN] = RawTextAnalyzerConsts.LiteCoinAddress
        self.regexp_map[CryptoCoinWordMatchType.RIPPLE] = RawTextAnalyzerConsts.RippleAddress
        self.regexp_map[CryptoCoinWordMatchType.BITCOIN_CASH] = RawTextAnalyzerConsts.BitCoinCashAddress
        self.regexp_map[CryptoCoinWordMatchType.WIF] = RawTextAnalyzerConsts.WifAddress
        self.regexp_map[CryptoCoinWordMatchType.XPUB] = RawTextAnalyzerConsts.Xpub
        self.regexp_map[CryptoCoinWordMatchType.CONTAINER] = RawTextAnalyzerConsts.Container
        self.regexp_map[CryptoCoinWordMatchType.CREDIT_CARD] = RawTextAnalyzerConsts.CreditCard_rlike


    def run(self, content: str) -> list[GoldenGateRow]:
        self.handle_row(content)

        return list(self.data)

    def run_on_list(self, contents: list[str]) -> list[GoldenGateRow]:
        self.data = set()
        for content in contents:
            self.handle_row(content)
        return list(self.data)
    
    def handle_row(self, row):
        try:
            self.handle_mnemonic(row)
            self.handle_bitcoin(row)
            self.handle_ethereum(row)
            self.handle_tron(row)
            self.handle_iban(row)
            self.handle_container(row)
            self.handle_monero(row)
            self.handle_zcash_z(row)
            self.handle_zcash_t(row)
            self.handle_litecoin(row)
            self.handle_ripple(row)
            self.handle_bitcoin_cash(row)
            self.handle_xpub(row)
            self.handle_wif(row)
            self.handle_creditcard(row)
        except Exception as e:
            print(e)


    def get_current_datetime(self):
        cur_dt = datetime.datetime.now()
        cur_dt_str = cur_dt.strftime("%Y%m%d")
        return cur_dt_str
    
    
    def handle_mnemonic(self, content):
        if CryptoCoinWordMatchType.MNEMONIC_PHRASE not in self.identifiers:
            return False

        phrase = str(content)
        match = re.search(RawTextAnalyzerConsts.Mnemonic, content)
        
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            words = phrase[start:end].split(' ')

            is_mnemonic, intersec_list, words_position_list = MnemonicValidator().check_for_mnemonic_words(words, 12)

            if is_mnemonic:
                mnemonic_ordered_list = []
                for index in words_position_list:
                    mnemonic_ordered_list.append(words[index])

                if " ".join(mnemonic_ordered_list) not in MnemonicValidator().mnemonic_black_list:
                    self.data.add(GoldenGateRow(
                        CryptoCoinWordMatchType.MNEMONIC_PHRASE, 
                        MatchGroupType.MNEMONIC_GROUP,
                        str(mnemonic_ordered_list)
                    ))


    def handle_bitcoin(self, content):
        if CryptoCoinWordMatchType.BITCOIN not in self.identifiers:
            return False

        match = re.search(RawTextAnalyzerConsts.BitcoinAddressCurrent, content)
        
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            word = content[start:end]

            if word.startswith(tuple(RawTextAnalyzerConsts.Base58PreFixList)) and self.check_base58_validity(word):
                self.data.add(GoldenGateRow(
                    CryptoCoinWordMatchType.BITCOIN_BASE58,
                    MatchGroupType.COINS_GROUP,
                    word
                ))

            if word.startswith(tuple(RawTextAnalyzerConsts.BECH32PrefixList)) and self.check_bech32_validity(word):
                self.data.add(GoldenGateRow(
                    CryptoCoinWordMatchType.BITCOIN_BECH32,
                    MatchGroupType.COINS_GROUP,
                    word
                ))


    def handle_ethereum(self, content):
        def exist_ethereum(ethereum_dict):
            for item in self.ethereum_data:
                if ethereum_dict == item:
                    return True   
            return False
        
        if CryptoCoinWordMatchType.ETHEREUM not in self.identifiers:
            return False

        match = re.search(RawTextAnalyzerConsts.EthereumAddress, content)
        
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            word = content[start:end]
            
            if word.startswith(tuple(RawTextAnalyzerConsts.EthereumPrefixList)) and self.check_ethereum_validity(word):
                self.data.add(GoldenGateRow(
                        CryptoCoinWordMatchType.ETHEREUM,
                        MatchGroupType.COINS_GROUP,
                        word
                ))                        


    def handle_tron(self, content):
        if CryptoCoinWordMatchType.TRON not in self.identifiers:
            return False

        match = re.search(RawTextAnalyzerConsts.Tron, content)
            
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            word = content[start:end]

            if word.startswith(tuple(RawTextAnalyzerConsts.TronPrefixList)) and self.check_tron_validity(word):
                self.data.add(GoldenGateRow(
                    CryptoCoinWordMatchType.TRON,
                    MatchGroupType.COINS_GROUP,
                    word
                ))


    def handle_iban(self, content):
        
        def exist_iban(iban_dict):
            for item in self.iban_data:
                if iban_dict == item:
                    return True
                
            return False

        if CryptoCoinWordMatchType.IBAN not in self.identifiers:
            return False

        match = re.search(RawTextAnalyzerConsts.Iban, content)
        
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            word = content[start:end].strip()

            if self.check_iban_validity(word):
                self.data.add(GoldenGateRow(
                    CryptoCoinWordMatchType.IBAN,
                    MatchGroupType.BANKING,
                    word
                ))


    def handle_container(self, content):
        if CryptoCoinWordMatchType.CONTAINER not in self.identifiers:
            return False

        match = re.search(RawTextAnalyzerConsts.Container, content)
        
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            word = content[start:end]

            if self.check_container_validity(word):
                self.data.add(GoldenGateRow(
                    CryptoCoinWordMatchType.CONTAINER,
                    MatchGroupType.COMMERCE,
                    word
                ))


    def handle_monero(self, content):
        if CryptoCoinWordMatchType.MONERO not in self.identifiers:
            return False

        match = re.search(RawTextAnalyzerConsts.MoneroAddress, content)
        
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            word = content[start:end]

            if self.check_monero_validity(word):
                self.data.add(GoldenGateRow(
                    CryptoCoinWordMatchType.MONERO,
                    MatchGroupType.COINS_GROUP,
                    word
                ))


    def handle_zcash_z(self, content):
        if CryptoCoinWordMatchType.ZCASH_Z not in self.identifiers:
            return False

        match = re.search(RawTextAnalyzerConsts.ZcashZAddress, content)
        
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            word = content[start:end]

            if self.check_bech32_validity(word):
                self.data.add(GoldenGateRow(
                    CryptoCoinWordMatchType.ZCASH_Z,
                    MatchGroupType.COINS_GROUP,
                    word
                ))


    def handle_zcash_t(self, content):
        if CryptoCoinWordMatchType.ZCASH_T not in self.identifiers:
            return False

        match = re.search(RawTextAnalyzerConsts.ZcashTAddress, content)
        
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            word = content[start:end]

            if self.check_base58_validity(word):
                self.data.add(GoldenGateRow(
                    CryptoCoinWordMatchType.ZCASH_T,
                    MatchGroupType.COINS_GROUP,
                    word
                ))


    def handle_litecoin(self, content):
        if CryptoCoinWordMatchType.LITECOIN not in self.identifiers:
            return False

        match = re.search(RawTextAnalyzerConsts.LiteCoinAddress, content)
        
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            word = content[start:end]

            if self.check_base58_validity(word):
                self.data.add(GoldenGateRow(
                    CryptoCoinWordMatchType.LITECOIN,
                    MatchGroupType.COINS_GROUP,
                    word
                ))


    def handle_ripple(self, content):
        if CryptoCoinWordMatchType.RIPPLE not in self.identifiers:
            return False

        match = re.search(RawTextAnalyzerConsts.RippleAddress, content)
        
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            word = content[start:end]

            if self.check_base58_validity(word, base58.RIPPLE_ALPHABET):
                self.data.add(GoldenGateRow(
                    CryptoCoinWordMatchType.RIPPLE,
                    MatchGroupType.COINS_GROUP,
                    word
                ))


    def handle_bitcoin_cash(self, content):
        if CryptoCoinWordMatchType.BITCOIN_CASH not in self.identifiers:
            return False

        match = re.search(RawTextAnalyzerConsts.BitCoinCashAddress, content)
        
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            word = content[start:end]

            full_word = RawTextAnalyzerConsts.BitCoinCashPrefixList[0] + word if not word.startswith(tuple(RawTextAnalyzerConsts.BitCoinCashPrefixList)) else word
            if self.check_bitcoin_cash_validity(full_word):
                self.data.add(GoldenGateRow(
                    CryptoCoinWordMatchType.BITCOIN_CASH,
                    MatchGroupType.COINS_GROUP,
                    word
                ))


    def handle_xpub(self, content):
        if CryptoCoinWordMatchType.XPUB not in self.identifiers:
            return False
            
        match = re.search(RawTextAnalyzerConsts.Xpub, content)
        
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            word = content[start:end]
            
            if self.check_base58_validity(word):
                self.data.add(GoldenGateRow(
                    CryptoCoinWordMatchType.XPUB,
                    MatchGroupType.XPUB_GROUP,
                    word
                ))


    def handle_wif(self, content):
        if CryptoCoinWordMatchType.WIF not in self.identifiers:
            return False

        match = re.search(RawTextAnalyzerConsts.WifAddress, content)
        
        if match is not None:
            start = match.regs[0][0]
            end = match.regs[0][1]
            word = content[start:end]

            if self.check_base58_validity(word):
                self.data.add(GoldenGateRow(
                    CryptoCoinWordMatchType.WIF,
                    MatchGroupType.COINS_GROUP,
                    word
                ))
    

    def handle_creditcard(self, content):
        
        def remove_special_chars(raw_text):
            for delimiter in self.special_chars_list:
                raw_text = raw_text.replace(delimiter, ' ') + "\t"
            return raw_text
        
        def exist_creditcard(creditcard_dict):
            for item in self.credircard_data:
                if creditcard_dict == item:
                    return True
                
            return False
        
        if CryptoCoinWordMatchType.CREDIT_CARD not in self.identifiers:
            return False
        
        match_cc = re.search(RawTextAnalyzerConsts.CreditCard_rlike, content)
        
        if match_cc is not None:
            if not any(blacklisted_word.lower() in content.lower() for blacklisted_word in self.black_list_words):
                word = remove_special_chars(content)
                
                for creditcard in [CryptoCoinWordMatchType.VISA,CryptoCoinWordMatchType.MASTERCARD]:
                    analyzer = RawTextAnalyzerConsts.Visa if creditcard == CryptoCoinWordMatchType.VISA else RawTextAnalyzerConsts.Mastercard
                    matches = re.finditer(analyzer, word)
                    
                    if matches is not None:
                        results = [str(match.group(1)) for match in matches]
                        
                        for result in results:
                            is_match = self.check_credit_card_validity(result) and self.check_credit_card_surrounding(result, word)
                            
                            if is_match:
                                self.data.add(GoldenGateRow(
                                    creditcard,
                                    MatchGroupType.CREDITCARD,
                                    result
                                ))
    

    def check_base58_validity(self, data, alphabet = base58.BITCOIN_ALPHABET):
        try:
            base58.b58decode_check(data, alphabet)
            return True
        except Exception:
            return False


    def check_ethereum_validity(self, data):
        try:
            if len(data) == 42:
                eth_utils.decode_hex(data)
                b = eth_utils.to_checksum_address(data)
                return eth_utils.is_checksum_formatted_address(b)
            
            return False
        except Exception:
            return False


    def check_tron_validity(self, data):
        if not isinstance(data, str):
            return False

        try:
            decode = base58.b58decode_check(data)
            return False if len(decode) != 21 or decode[0] != 0x41 else True
        except Exception:
            return False


    def check_bitcoin_cash_validity(self, data):
        try:
            bitcoincash.cashaddr.decode(data)
            return True
        except Exception:
            return False


    def check_bech32_validity(self, data):
        try:
            bech32.bech32_decode(data)
            return True
        except Exception:
            return False


    def check_monero_validity(self, data):
        try:
            monero.address.base58.decode(data)
            return True
        except Exception:
            return False


    def check_iban_validity(self, data):
        if data[:2].upper() == 'IR':
            def check_validation_chars_iban(iban):
                zeros_iban = iban[:2] + '00' + iban[4:]
                iban_inverted = zeros_iban[4:] + zeros_iban[:4]
                iban_numbered = iban_inverted.translate(self.characters_map)
                verification_chars = 98 - (int(iban_numbered) % 97)

                if verification_chars < 10:
                    verification_chars = int('{:02}'.format(verification_chars))

                return verification_chars

            def validate_iban(iban):
                iban_inverted = iban[4:] + iban[:4]
                iban_numbered = iban_inverted.translate(self.characters_map)

                return int(iban_numbered) % 97

            try:
                _iban = data.upper()
                if check_validation_chars_iban(_iban) == int(_iban[2:4]):
                    return validate_iban(_iban) == 1
                else:
                    return False
            except:
                return False
        else:   
            try:
                check_iban = IBAN(data)
                check_iban.validate()
                return True
            except:
                return False


    def check_container_validity(self, data):
        container_value = 0
        multiplier = 1 
        og_check_digit = int(data[-1])

        for letter in data[:4]:
            container_value += self.alpha_map[letter] * multiplier
            multiplier *= 2
        for digit in data[4:10]:
            container_value += (int(digit) * multiplier)
            multiplier *= 2

        check_digit = container_value - (container_value // 11) * 11
        if check_digit == 10:
            check_digit = 0

        return check_digit == og_check_digit
    
    
    def check_credit_card_validity(self, cardNo):
        nDigits = len(cardNo)
        nSum = 0
        isSecond = False
        for i in range(nDigits -1, -1, -1):
            d=ord(cardNo[i]) - ord('0')
            if isSecond == True:
                d=d*2
            nSum +=d // 10
            nSum += d % 10

            isSecond = not isSecond

        if nSum % 10 == 0:
            return True
        else:
            return False


    def check_credit_card_surrounding(self, data, content):
        card_idx = content.index(data)

        if data == content:
            return True

        try:
            if card_idx == 0:
                return content[card_idx + len(data)] in self.credit_card_chars
            
            return content[card_idx - 1] in self.credit_card_chars and content[card_idx + len(data)] in self.credit_card_chars
        except Exception as e:
            return False