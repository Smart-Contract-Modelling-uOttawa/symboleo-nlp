from typing import List, Dict
from app.classes.operations.user_input import UserInput
from app.classes.units.unit_type import UnitType
from app.classes.units.all_units import unit_type_dict

from app.src.selection.child_node_getter import IGetNodeChildren

from app.web_lib.contract_storage import ContractStorage
from app.web_lib.input_storage import InputStorage

class ValueProcessor:
    def __init__(
        self, 
        child_getter: IGetNodeChildren,
        contract_storage: ContractStorage,
        input_storage: InputStorage
    ):
        self.__child_getter = child_getter
        self.__contract_storage = contract_storage
        self.__input_storage = input_storage

    def process(self, contract_id: str, input_id: str, value: str, unique_key:str) -> Dict[str, List[str]]:
        # Get the input type
        unit_type = UnitType[input_id] 
        user_input = UserInput(unit_type, value)

        # Extract the element
        self.__input_storage.add_input(unique_key, user_input)

        # Get the contract
        contract = self.__contract_storage.load(unique_key, contract_id)

        # Fetch the children
        input_unit = unit_type_dict[unit_type]()
        children = self.__child_getter.get(input_unit, contract)
        #result = [x.unit_type.name for x in children]

        result = {
            x.unit_type.name: x.options
            for x in children  
        }

        # What if there are no children...? That will probably be separate
        return result


        

