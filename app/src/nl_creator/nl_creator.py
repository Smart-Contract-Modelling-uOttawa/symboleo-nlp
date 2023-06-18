from typing import List, Dict
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.user_input import UnitType, UserInput
from app.src.nl_creator.nl_fillers.nl_unit_filler_dict import IFillNLUnit

class ICreateNL:
    def create(self, contract: SymboleoContract, input_list: List[UserInput]) -> str:
        raise NotImplementedError()

# TODO: Will probably get rid of this in favour of the pattern_updater

class NLCreator(ICreateNL):
    def __init__(
        self, 
        nl_filler_dict: Dict[UnitType, IFillNLUnit]
    ):
        self.__dict = nl_filler_dict

    def create(self, contract: SymboleoContract, input_list: List[UserInput]) -> str:
        result = []

        # iterate through each of the patterns, and fill the required pieces
        for i, user_input in enumerate(input_list):
            next_op = self.__dict[user_input.unit_type]
            result = next_op.fill(contract, result, input_list, i)
        
        # This is where can put punctuation etc
        return ' '.join(result)

