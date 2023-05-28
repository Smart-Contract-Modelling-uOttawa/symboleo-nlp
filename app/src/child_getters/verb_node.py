from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.custom_event.verb import Verb, VerbType
from app.classes.units.custom_event_node import *
from app.classes.elements.custom_event_node import VerbNode

from app.classes.units.all_nodes import VerbNode as VerbToken

from app.src.child_getters.child_getter import IGetNodeChildren

class VerbNodeCG(IGetNodeChildren):
    def get(self, parent_node: VerbToken, contract: ISymboleoContract, prev_value: VerbNode) -> List[InputUnit]:
        verb_types = prev_value.value.verb_types
        children = []
        if VerbType.LINKING in verb_types:
            children.append(PredicateNode())
        
        if VerbType.TRANSITIVE in verb_types:
            children.append(DobjNode())
        
        if VerbType.INTRANSITIVE in verb_types:
            children.append(AdverbNode())
            children.append(FinalNode())
    
        return children

