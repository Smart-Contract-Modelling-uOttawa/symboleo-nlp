from typing import List
from app.classes.units.input_unit import InputUnit
from app.src.selection.token_selector_set import ISelectNode

# TODO: Move into console app
class ManualNodeSelector(ISelectNode):
    def select(self, unit_set: List[InputUnit]) -> InputUnit:
        if len(unit_set) == 1:
            return unit_set[0]
        
        print('\nChoose an option:')
        unit_dict = {i+1: unit_set[i] for i in range(0, len(unit_set))}

        # User selects next child
        for ci in unit_dict:
            cn = unit_dict[ci]
            print('-', ci, cn.prompt)

        print('\n')
        
        # Get the value. Sometimes auto, sometimes from user
        k = input("Enter target id: ")
        result = unit_dict[int(k)]
        return result