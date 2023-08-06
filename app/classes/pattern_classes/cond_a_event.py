from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV
from app.classes.events.conj_type import ConjType

class CondAEvent(EventPatternClass):
    sequence = [PV.CONDITIONAL_A, PV.EVENT]
    conj_type = ConjType.PRESENT
