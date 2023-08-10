from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV
from app.classes.events.conj_type import ConjType

class CondTEvent(EventPatternClass):
    sequence = [PV.CONDITIONAL_T, PV.EVENT]
    conj_type = ConjType.PRESENT

