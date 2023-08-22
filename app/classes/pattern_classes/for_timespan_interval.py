from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class ForTimespanInterval(EventPatternClass):
    sequence = [PV.FOR, PV.TIMESPAN, PV.AFTER, PV.EVENT]