from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV

class AfterDate(PatternClass):
    sequence = [PV.P_AFTER, PV.DATE]
    