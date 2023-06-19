from typing import Type, DefaultDict
from collections import defaultdict
from app.classes.units.input_unit import InputUnit
from app.classes.units.all_units import *

from app.src.selection.child_getters.child_getter import IGetUnitChildren, DefaultChildGetter
from app.src.selection.child_getters.standard_event_unit_cg import StandardEventUnitCG
from app.src.selection.child_getters.norm_event_unit_cg import NormEventUnitCG
from app.src.selection.child_getters.obligation_subject_unit_cg import ObligationSubjectUnitCG
from app.src.selection.child_getters.custom_event_unit_cg import CustomEventUnitCG
from app.src.selection.child_getters.t_verb_unit_cg import TVerbUnitCG
from app.src.selection.child_getters.before_unit_cg import BeforeUnitCG

# Helpers (injected)
from app.src.selection.child_getters.domain_timepoint_extractor import DomainTimepointExtractor

class ChildGetterDictConstructor:
    @staticmethod
    def build() -> DefaultDict[Type[InputUnit], IGetUnitChildren]:
        # Injection...?
        dtp_extractor = DomainTimepointExtractor()
        
        d = defaultdict(lambda: DefaultChildGetter())

        d[StandardEventUnit] = StandardEventUnitCG()
        d[NormEventUnit] = NormEventUnitCG()
        d[ObligationSubjectUnit] = ObligationSubjectUnitCG()
        d[TransitiveVerbUnit] = TVerbUnitCG()
        d[BeforeUnit] = BeforeUnitCG(dtp_extractor)

        d[CustomEventUnit] = CustomEventUnitCG()

        # Others to add: Power ones

        return d