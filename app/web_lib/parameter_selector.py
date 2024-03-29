from typing import List, Dict
from app.web_lib.cache.contract_storage import ContractStorage
from app.web_lib.cache.input_storage import InputStorage
from app.web_lib.grammar_handler import GrammarHandler

class ParameterSelector:
    def __init__(
        self,
        contract_storage: ContractStorage,
        input_storage: InputStorage,
        grammar_handler: GrammarHandler
    ):
        self.__contract_storage = contract_storage
        self.__input_storage = input_storage
        self.__grammar_handler = grammar_handler

    def select(self, contract_id: str, unique_key:str, nl_key:str, parm_key:str) -> Dict[str, any]:
        self.__input_storage.init_input(unique_key)

        contract = self.__contract_storage.load(unique_key, contract_id)

        parm = contract.nl_template.template_dict[nl_key].parameters[parm_key][0]
        
        # May combine these two
        self.__grammar_handler.create(unique_key, parm.pattern_types)
        children = self.__grammar_handler.get_children(unique_key, contract)

        result = {
            x.unit_type.name: x.to_dict()
            for x in children  
        }

        return result


        

