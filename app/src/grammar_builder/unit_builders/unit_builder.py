from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.input_unit import InputUnit

from app.classes.units.all_units import unit_type_dict, UnitType

class IBuildUnit:
    def build(self, unit_name:str, contract: ISymboleoContract) -> InputUnit:
        raise NotImplementedError()


class DefaultUnitBuilder(IBuildUnit):
    def build(self, unit_name:str, contract: ISymboleoContract) -> InputUnit:
        unit_type = UnitType[unit_name]
        return unit_type_dict[unit_type]()
    
