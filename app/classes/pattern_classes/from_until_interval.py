from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV

class FromUntilInterval(PatternClass):
    sequence = [PV.FROM_TIMEPOINT, PV.UNTIL_TIMEPOINT]

    def __init__(self) -> None:
        super().__init__()
        self.keyword1 = ''
        self.timepoint1 = ''
        self.keyword2 = ''
        self.timepoint2 = ''
    
    def to_text(self) -> str:
        return f'{self.keyword1} {self.timepoint1} {self.keyword2} {self.timepoint2}'
    