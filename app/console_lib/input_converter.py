from app.classes.grammar.grammar_node import GrammarNode
from app.classes.operations.user_input import UserInput
from app.classes.units.unit_type import UnitType, UnitVariety

from app.classes.units.all_units import unit_type_dict

class IConvertNodeToInput:
    def convert(self, node: GrammarNode) -> UserInput:
        raise NotImplementedError()

# TODO: Could add the child_getter so I can populate the options
## Also need to pass in the contract
class InputConverter(IConvertNodeToInput):
    def convert(self, node: GrammarNode) -> UserInput:
        unit_type = UnitType[node.name]
        unit = unit_type_dict[unit_type]

        # Dynamic
        if unit.unit_var == UnitVariety.DYNAMIC:
            value = input(f'\nEnter value for {unit.unit_type}: ')
        else:
            # Empty
            if unit.unit_var == UnitVariety.EMPTY:
                value = None
            else:
                # Static
                value = unit.init_value
        
        return UserInput(unit_type, value)

            
