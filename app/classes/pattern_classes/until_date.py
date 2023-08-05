from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV

class UntilDate(PatternClass):
    sequence = [PV.UNTIL, PV.DATE]
