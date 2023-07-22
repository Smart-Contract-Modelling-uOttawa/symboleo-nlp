from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.sym_event import ObligationEventName
from app.classes.units.input_unit import InputUnit
from app.classes.units.all_units import ObligationActionUnit

from app.src.grammar_builder.unit_builders.unit_builder import IBuildUnit

class ObligationActionUB(IBuildUnit):
    def build(self, unit_name: str, contract: SymboleoContract) -> InputUnit:
        opts = [str(x.value).lower() for x in ObligationEventName]            
        return ObligationActionUnit(opts)
