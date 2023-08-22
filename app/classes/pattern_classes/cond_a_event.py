from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class CondAEvent(EventPatternClass):
    sequence = [PV.CONDITIONAL_A, PV.EVENT]
