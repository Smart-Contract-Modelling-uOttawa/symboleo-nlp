from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.units.custom_event_units import *

from app.src.selection.child_getters.child_getter import IGetUnitChildren

class VerbUnitCG(IGetUnitChildren):
    def get(self, parent_unit: VerbUnit, contract: ISymboleoContract) -> List[InputUnit]:
        children = [PredicateUnit(), DobjUnit(), AdverbUnit()]
        # if VerbType.LINKING in verb_types:
        #     children.append(PredicateUnit())
        
        # if VerbType.TRANSITIVE in verb_types:
        #     children.append(DobjUnit())
        
        # if VerbType.INTRANSITIVE in verb_types:
        #     children.append(AdverbUnit())
        #     children.append(FinalUnit())
    
        return children

