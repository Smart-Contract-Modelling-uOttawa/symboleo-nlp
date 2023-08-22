from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.declaration import Declaration, DeclarationType
from app.classes.units.input_unit import InputUnit

from app.classes.units.all_units import SubjectUnit

from app.src.grammar_builder.unit_builders.unit_builder import IBuildUnit

class SubjectUB(IBuildUnit):
    def build(self, unit_name: str, contract: SymboleoContract) -> InputUnit:
        decls: List[Declaration] = contract.contract_spec.declarations.values()
        roles = [x.name for x in decls if x.base_type == DeclarationType.ROLE]
        assets = [x.name for x in decls if x.base_type == DeclarationType.ASSET]
        
        options = roles + assets

        return SubjectUnit(options)


