from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV

class BetweenInterval(PatternClass):
    sequence = [PV.BETWEEN, PV.DATE, PV.AND, PV.DATE2]
