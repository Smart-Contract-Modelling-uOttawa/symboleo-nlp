from typing import DefaultDict
from collections import defaultdict
from app.classes.units.all_units import *
from app.classes.units.unit_type import UnitType

from app.classes.operations.dependencies import Dependencies
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit, DefaultPatternFiller
from app.src.pattern_builder.pattern_unit_fillers.custom_event_filler import CustomEventFiller

from app.src.pattern_builder.pattern_unit_fillers.obligation_action_filler import ObligationActionFiller
from app.src.pattern_builder.pattern_unit_fillers.obligation_subject_filler import ObligationSubjectFiller

from app.src.custom_event_extractor.custom_event_extractor_builder import CustomEventExtractorBuilder

class PatternUnitFillerDictConstructor:
    @staticmethod
    def build(deps: Dependencies) -> DefaultDict[UnitType, IFillPatternUnit]:
        d = defaultdict(lambda: DefaultPatternFiller())
        
        event_extractor = CustomEventExtractorBuilder.build(deps)

        d[UnitType.CUSTOM_EVENT] = CustomEventFiller(event_extractor)
        d[UnitType.OBLIGATION_ACTION] = ObligationActionFiller()
        d[UnitType.OBLIGATION_SUBJECT] = ObligationSubjectFiller()

        return d