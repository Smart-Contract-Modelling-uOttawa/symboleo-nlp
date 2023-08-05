from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class BeforeEvent(EventPatternClass):
    sequence = [PV.P_BEFORE_E, PV.EVENT]
