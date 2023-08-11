from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.declaration import Declaration
from app.classes.spec.point_function import TimeUnit
from app.classes.units.input_unit import InputUnit
from app.classes.units.all_units import NotifierUnit

from app.src.grammar_builder.unit_builders.unit_builder import IBuildUnit

class NotifierUnitUB(IBuildUnit):
    def build(self, unit_name: str, contract: SymboleoContract) -> InputUnit:
        decls: List[Declaration] = contract.contract_spec.declarations.values()
        roles = [x.name for x in decls if x.base_type == 'roles']
        return NotifierUnit(roles)
