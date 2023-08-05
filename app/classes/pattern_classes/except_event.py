from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class ExceptEvent(EventPatternClass):
    sequence = [PV.P_EXCEPT, PV.EVENT]
