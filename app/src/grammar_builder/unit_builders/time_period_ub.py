from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.units.all_units import TimePeriodUnit

from app.src.grammar_builder.unit_builders.unit_builder import IBuildUnit

from app.src.object_mappers.time_period_mapper import TimePeriod

class TimePeriodUB(IBuildUnit):
    def build(self, unit_name: str, contract: SymboleoContract) -> InputUnit:
        opts = list(TimePeriod.time_period_dict().keys())
        return TimePeriodUnit(opts)
