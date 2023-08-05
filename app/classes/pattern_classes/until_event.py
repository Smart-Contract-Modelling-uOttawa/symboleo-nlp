from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class UntilEvent(EventPatternClass):
    sequence = [PV.UNTIL, PV.EVENT]
