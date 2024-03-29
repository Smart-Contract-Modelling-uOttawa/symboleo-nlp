from app.classes.spec.symboleo_contract import ISymboleoContract, SymboleoContract
from app.classes.spec.sym_event import ContractEventName
from app.classes.units.input_unit import InputUnit
from app.classes.units.all_units import ContractActionUnit

from app.src.grammar_builder.unit_builders.unit_builder import IBuildUnit


class ContractActionUB(IBuildUnit):

    def build(self, unit_name: str, contract: ISymboleoContract) -> InputUnit:
        #verbs = ['activate', 'terminate']
        opts = ['activating', 'activates', 'activated', 'terminated', 'terminating', 'terminates', 'terminated']

        #opts = [str(x.value).lower() for x in ContractEventName]            
        return ContractActionUnit(opts)
