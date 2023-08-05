from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class AfterEvent(EventPatternClass):
    sequence = [PV.P_AFTER_E, PV.EVENT]
