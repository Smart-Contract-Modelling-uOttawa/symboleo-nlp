from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.root_unit import RootUnit

from app.src.selection.child_node_getter import IGetNodeChildren
from app.web_lib.contract_storage import ContractStorage
from app.web_lib.input_storage import InputStorage

class ParameterSelector:
    def __init__(
        self, 
        child_getter: IGetNodeChildren,
        contract_storage: ContractStorage,
        input_storage: InputStorage
    ):
        self.__child_getter = child_getter
        self.__contract_storage = contract_storage
        self.__input_storage = input_storage

    def select(self, contract_id: str, unique_key:str):
        root_unit = RootUnit()

        self.__input_storage.init_input(unique_key)

        contract = self.__contract_storage.load(unique_key, contract_id)

        children = self.__child_getter.get(root_unit, None, contract)
        result = [x.unit_type.name for x in children]
        return result


        

