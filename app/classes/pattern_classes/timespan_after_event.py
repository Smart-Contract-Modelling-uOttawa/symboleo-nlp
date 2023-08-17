from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class TimespanAfterEvent(EventPatternClass):
    sequence = [PV.AT_LEAST, PV.TIMESPAN, PV.P_AFTER_T, PV.EVENT]

