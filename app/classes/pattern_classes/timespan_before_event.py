from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class TimespanBeforeEvent(EventPatternClass):
    sequence = [PV.TIMESPAN, PV.P_BEFORE_T, PV.EVENT]

