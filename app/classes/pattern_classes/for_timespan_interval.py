from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV

class ForTimespanInterval(PatternClass):
    sequence = [PV.FOR, PV.TIMESPAN, PV.AFTER, PV.TIMEPOINT]
