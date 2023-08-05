from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV

class FromUntilInterval(PatternClass):
    sequence = [PV.FROM, PV.TIMEPOINT, PV.UNTIL, PV.TIMEPOINT2]
