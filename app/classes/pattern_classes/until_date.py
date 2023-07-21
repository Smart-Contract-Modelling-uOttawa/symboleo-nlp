from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV


class UntilDate(PatternClass):
    sequence = [PV.UNTIL, PV.DATE]
    
    def __init__(self):
        super().__init__()
        self.date_text = ''
    
    def to_text(self) -> str:
        return f'{self.keyword} {self.date_text}'