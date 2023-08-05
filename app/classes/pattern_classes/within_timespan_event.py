from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV
from app.classes.events.conj_type import ConjType

class WithinTimespanEvent(EventPatternClass):
    sequence = [PV.WITHIN, PV.TIMESPAN, PV.P_AFTER_W, PV.EVENT]
    conj_type = ConjType.CONTINUOUS
