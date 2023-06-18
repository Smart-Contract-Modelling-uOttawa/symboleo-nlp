from typing import DefaultDict
from collections import defaultdict
from app.classes.units.all_units import *
from app.classes.units.unit_type import UnitType

from app.src.nl_creator.nl_fillers.nl_unit_filler import IFillNLUnit, DefaultNLFiller, SkipFiller
from app.src.nl_creator.nl_fillers.obligation_subject_filler import ObligationSubjectFiller

class NLUnitFillerDictConstructor:
    @staticmethod
    def build() -> DefaultDict[UnitType, IFillNLUnit]:
        d = defaultdict(lambda: DefaultNLFiller())
        skip_filler = SkipFiller()
        
        d[UnitType.CUSTOM_EVENT] = skip_filler
        d[UnitType.OBLIGATION_ACTION] = skip_filler
        d[UnitType.OBLIGATION_SUBJECT] = ObligationSubjectFiller()

        return d