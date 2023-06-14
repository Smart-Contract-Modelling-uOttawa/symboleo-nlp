import simple_cache

from app.classes.spec.symboleo_contract import SymboleoContract

class ContractStorage:
    def __init__(self):
        self.__ttl = 20000
        self.__cache_name = 'contract.cache'

    def store(self, unique_key:str, contract_id:str, contract: SymboleoContract):
        simple_cache.save_key(self.__cache_name, f'{unique_key}.{contract_id}', contract, self.__ttl)
    

    def load(self, unique_key:str, contract_id:str):
        result: SymboleoContract = simple_cache.load_key(self.__cache_name, f'{unique_key}.{contract_id}')
        return result