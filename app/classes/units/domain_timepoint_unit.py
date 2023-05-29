from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

class DomainTimepointUnit(InputUnit):
    unit_type = UnitType.DOMAIN_TIMEPOINT
    prompt = 'Domain timepoint...'
    needs_value = True
    
    # TODO: Not sure how this will work, especially with options..
    ## Might init with the contract...
    # def __init__(self, id: str, children: List[InputUnit] = [], init_value: str = ''):
    #     super().__init__(id, children)
    #     self.prompt = init_value
    #     self.init_value = init_value

    