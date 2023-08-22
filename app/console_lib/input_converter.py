from app.classes.operations.user_input import UserInput
from app.classes.units.unit_variety import UnitVariety
from app.classes.units.input_unit import InputUnit

class IConvertNodeToInput:
    def convert(self, input_unit: InputUnit) -> UserInput:
        raise NotImplementedError()

class InputConverter(IConvertNodeToInput):
    def convert(self, input_unit: InputUnit) -> UserInput:
        # Dynamic
        if input_unit.unit_var == UnitVariety.DYNAMIC:
            prompt = f'\nEnter value for {input_unit.unit_type}: \n'
            
            if input_unit.options:
                for x in input_unit.options:
                    prompt += f'- {x}\n'
            
            print(prompt)
            value = input('\nEnter value: ')

        else:
            # Empty
            if input_unit.unit_var == UnitVariety.EMPTY:
                value = None
            else:
                # Static
                value = input_unit.init_value
        
        return UserInput(input_unit.unit_type, value)

            
