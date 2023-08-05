from typing import DefaultDict
from collections import defaultdict
from app.classes.units.all_units import *

from app.src.grammar_builder.unit_builders.unit_builder import IBuildUnit, DefaultUnitBuilder
from app.src.grammar_builder.unit_builders.subject_ub import SubjectUB
from app.src.grammar_builder.unit_builders.dobj_ub import DobjUB
from app.src.grammar_builder.unit_builders.obligation_subject_ub import ObligationSubjectUB
from app.src.grammar_builder.unit_builders.obligation_action_ub import ObligationActionUB
from app.src.grammar_builder.unit_builders.time_unit_ub import TimeUnitUB

# Helpers (injected)
#from app.src.selection.child_getters.domain_timepoint_extractor import DomainTimepointExtractor

class UnitBuilderDictConstructor:
    @staticmethod
    def build() -> DefaultDict[UnitType, IBuildUnit]:
        # # Injection...?
        # dtp_extractor = DomainTimepointExtractor()
        
        d = defaultdict(lambda: DefaultUnitBuilder())

        d[UnitType.SUBJECT] = SubjectUB()
        d[UnitType.DOBJ] = DobjUB()
        d[UnitType.OBLIGATION_SUBJECT] = ObligationSubjectUB()
        d[UnitType.OBLIGATION_ACTION] = ObligationActionUB()
        d[UnitType.TIME_UNIT] = TimeUnitUB()

        return d