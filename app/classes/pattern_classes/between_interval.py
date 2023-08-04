from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV

# TODO: Work to do on this...
class BetweenInterval(PatternClass):
    sequence = [PV.BETWEEN, PV.TIMEPOINT, PV.AND, PV.TIMEPOINT2]

    # def __init__(self) -> None:
    #     super().__init__()
    #     self.keyword1 = ''
    #     self.timepoint1 = ''
    #     self.keyword2 = ''
    #     self.timepoint2 = ''
    
    # def to_text(self) -> str:
    #     return f'{self.keyword1} {self.timepoint1} {self.keyword2} {self.timepoint2}'
    