from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.declaration import Declaration
from app.classes.spec.sym_event import ObligationEventName
from app.classes.units.input_unit import InputUnit
from app.classes.elements.element import Element

from app.classes.units.all_units import TransitiveVerbUnit, DobjUnit

from app.src.selection.child_getters.child_getter import IGetUnitChildren

class TVerbUnitCG(IGetUnitChildren):
    def get(self, parent_unit: TransitiveVerbUnit, contract: SymboleoContract) -> List[InputUnit]:
        decls: List[Declaration] = contract.contract_spec.declarations.values()
        roles = [x.name for x in decls if x.base_type == 'roles']
        assets = [x.name for x in decls if x.base_type == 'assets']
        
        subj_children = roles + assets

        return [
            DobjUnit(subj_children)
        ]


