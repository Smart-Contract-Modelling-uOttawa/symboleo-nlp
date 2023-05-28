from typing import List, Type, DefaultDict
from collections import defaultdict
from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType
from app.classes.units.all_nodes import *

from app.src.child_getters.child_getter import IGetNodeChildren, DefaultChildGetter

from app.src.child_getters.standard_event_node import StandardEventNodeCG
from app.src.child_getters.norm_event_node import NormEventNodeCG
from app.src.child_getters.obligation_subject_node import ObligationSubjectNodeCG
from app.src.child_getters.custom_event_node import CustomEventNodeCG
from app.src.child_getters.verb_node import VerbNodeCG
from app.src.child_getters.before_node import BeforeNodeCG

# Helpers (injected)
from app.src.child_getters.domain_timepoint_extractor import DomainTimepointExtractor

class ChildGetterDictConstructor:
    @staticmethod
    def build() -> DefaultDict[Type[InputUnit], IGetNodeChildren]:
        # Injection...?
        dtp_extractor = DomainTimepointExtractor()
        
        d = defaultdict(lambda: DefaultChildGetter())

        d[StandardEventNode] = StandardEventNodeCG()
        d[NormEventNode] = NormEventNodeCG()
        d[ObligationSubjectNode] = ObligationSubjectNodeCG()
        d[VerbNode] = VerbNodeCG()
        d[BeforeNode] = BeforeNodeCG(dtp_extractor)

        # CommonEvent
        d[CommonEventNode] = CustomEventNodeCG()
        d[CustomEventNode] = CustomEventNodeCG()

        # Others to add: Power ones

        return d