from app.classes.units.input_unit import InputUnit
from app.classes.operations.user_input import UserInput

# May move this to user_scripts... its an I/O concern
class IGetInputValues:
    def get(self, unit: InputUnit) -> UserInput:
        raise NotImplementedError()

class InputValueGetter(IGetInputValues):
    def get(self, unit: InputUnit) -> str:
        if not unit.needs_value:
            str_val = unit.init_value
        else:
            
            if unit.options:
                print(f'\noptions for {unit.unit_type.value}')
                for x in unit.options:
                    print(f'- {x}')
            

            str_val = input(f'{unit.prompt}: ')


        return UserInput(unit.unit_type, str_val)