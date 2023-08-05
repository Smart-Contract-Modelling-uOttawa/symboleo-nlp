from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class WithinTimespanEvent(EventPatternClass):
    sequence = [PV.WITHIN, PV.TIMESPAN, PV.P_AFTER_W, PV.EVENT]
