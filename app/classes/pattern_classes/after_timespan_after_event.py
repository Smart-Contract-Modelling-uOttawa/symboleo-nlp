from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV
from app.classes.events.conj_type import ConjType

class AfterTimespanAfterEvent(EventPatternClass):
    sequence = [PV.P_AFTER_PF, PV.TIMESPAN, PV.P_AFTER_T, PV.EVENT]
    conj_type = ConjType.PRESENT
