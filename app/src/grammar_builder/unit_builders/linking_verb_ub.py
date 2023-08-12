from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.units.all_units import LinkingVerbUnit

from app.src.grammar_builder.unit_builders.unit_builder import IBuildUnit

class LinkingVerbUB(IBuildUnit):
    def build(self, unit_name: str, contract: SymboleoContract) -> InputUnit:
        opts = ['become', 'becomes']            
        # Could make use of VerbLists.linking_verbs...
        return LinkingVerbUnit(opts)
