from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class CondTEvent(EventPatternClass):
    sequence = [PV.CONDITIONAL_T, PV.EVENT]
