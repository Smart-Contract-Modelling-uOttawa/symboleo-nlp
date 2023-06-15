from typing import DefaultDict
from collections import defaultdict
from app.classes.units.all_units import *
from app.classes.units.unit_type import UnitType

from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit, DefaultPatternFiller

from app.src.pattern_builder.pattern_unit_fillers.custom_event_filler import CustomEventFiller
from app.src.pattern_builder.pattern_unit_fillers.timespan_filler import TimespanFiller
from app.src.pattern_builder.pattern_unit_fillers.date_filler import DateFiller

from app.src.pattern_builder.pattern_unit_fillers.obligation_action_filler import ObligationActionFiller
from app.src.pattern_builder.pattern_unit_fillers.obligation_subject_filler import ObligationSubjectFiller

class PatternUnitFillerDictConstructor:
    @staticmethod
    def build() -> DefaultDict[UnitType, IFillPatternUnit]:
        d = defaultdict(lambda: DefaultPatternFiller())
        
        d[UnitType.CUSTOM_EVENT] = CustomEventFiller()
        d[UnitType.TIMESPAN] = TimespanFiller()
        d[UnitType.DATE] = DateFiller()

        d[UnitType.OBLIGATION_ACTION] = ObligationActionFiller()
        d[UnitType.OBLIGATION_SUBJECT] = ObligationSubjectFiller()

        return d