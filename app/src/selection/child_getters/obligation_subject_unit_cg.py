from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.sym_event import ObligationEventName
from app.classes.units.input_unit import InputUnit
from app.classes.elements.element import Element

from app.classes.units.all_units import ObligationSubjectUnit, ObligationActionUnit

from app.src.selection.child_getters.child_getter import IGetUnitChildren

class ObligationSubjectUnitCG(IGetUnitChildren):
    def get(self, parent_unit: ObligationSubjectUnit, contract: SymboleoContract, element: Element) -> List[InputUnit]:
        opts = [str(x.value).lower() for x in ObligationEventName]
            
        node1 = ObligationActionUnit(opts)

        return [node1]

