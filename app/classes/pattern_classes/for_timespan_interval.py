from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass, PatternVariable as PV
from app.classes.events.conj_type import ConjType

class ForTimespanInterval(EventPatternClass):
    sequence = [PV.FOR, PV.TIMESPAN, PV.AFTER, PV.EVENT]
    conj_type = ConjType.PRESENT