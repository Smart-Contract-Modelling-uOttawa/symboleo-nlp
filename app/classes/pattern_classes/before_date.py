from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV

class BeforeDate(PatternClass):
    sequence = [PV.P_BEFORE_S, PV.DATE]
    