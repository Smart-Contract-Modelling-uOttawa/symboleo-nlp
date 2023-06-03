import copy
from typing import List
from app.classes.operations.user_input import UserInput
from app.classes.units.unit_type import UnitType

# Adds any needed values to user input - mainly for testing
## Allows us to enter UserInput(WITHIN), without specifying the 'within' value
## This class just pads those values
class ICleanUserInput:
    def clean(self, user_inputs: List[UserInput]):
        raise NotImplementedError()

class UserInputCleaner(ICleanUserInput):
    def __init__(self):
        self._value_dict = {
            UnitType.UNLESS: 'unless',
            UnitType.WITHIN: 'within',
            UnitType.BEFORE: 'before',
            UnitType.AFTER: 'after',
            UnitType.UNTIL: 'until',
            UnitType.FOLLOWING: 'following',
            UnitType.FOR: 'for',
            UnitType.IF: 'if',
            UnitType.OF: 'of',
            UnitType.WHEN: 'when',
            UnitType.CONTRACT_SUBJECT: 'contract',
            UnitType.FAILS_TO: 'fails to'
        }

    def clean(self, user_inputs: List[UserInput]):
        result = copy.deepcopy(user_inputs)

        for x in result:
            if x.unit_type in self._value_dict:
                x.value = self._value_dict[x.unit_type]
        
        return result


