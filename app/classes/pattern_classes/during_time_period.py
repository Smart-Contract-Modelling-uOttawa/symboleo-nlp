from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV

class DuringTimePeriod(PatternClass):
    sequence = [PV.P_DURING, PV.TIME_PERIOD]

    def __init__(self) -> None:
        super().__init__()
        self.keyword = ''
        self.time_period = ''
    
    def to_text(self) -> str:
        return f'{self.keyword} {self.time_period}'
    