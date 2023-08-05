from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class AfterTimespanBeforeEvent(EventPatternClass):
    sequence = [PV.P_AFTER_PF, PV.TIMESPAN, PV.P_BEFORE_T, PV.EVENT]
