from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class AfterTimespanAfterEvent(EventPatternClass):
    sequence = [PV.P_AFTER_PF, PV.TIMESPAN, PV.P_AFTER_T, PV.EVENT]
