from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.point_function import TimeUnit
from app.classes.units.input_unit import InputUnit
from app.classes.units.all_units import TimeUnitUnit

from app.src.grammar_builder.unit_builders.unit_builder import IBuildUnit

class TimeUnitUB(IBuildUnit):
    def build(self, unit_name: str, contract: SymboleoContract) -> InputUnit:
        opts = [str(x.value).capitalize() for x in TimeUnit]            
        return TimeUnitUnit(opts)
