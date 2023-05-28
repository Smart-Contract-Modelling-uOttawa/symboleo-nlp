from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.custom_event.verb import Verb, VerbType
from app.classes.units.custom_event_units import *
from app.classes.elements.custom_event_elements import VerbElement

from app.classes.units.all_units import VerbUnit

from app.src.child_getters.child_getter import IGetUnitChildren

class VerbUnitCG(IGetUnitChildren):
    def get(self, parent_unit: VerbUnit, contract: ISymboleoContract, element: VerbElement) -> List[InputUnit]:
        verb_types = element.value.verb_types
        children = []
        if VerbType.LINKING in verb_types:
            children.append(PredicateUnit())
        
        if VerbType.TRANSITIVE in verb_types:
            children.append(DobjUnit())
        
        if VerbType.INTRANSITIVE in verb_types:
            children.append(AdverbUnit())
            children.append(FinalUnit())
    
        return children

