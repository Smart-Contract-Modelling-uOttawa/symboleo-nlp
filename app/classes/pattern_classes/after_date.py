from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV


class AfterDate(PatternClass):
    sequence = [PV.P_AFTER, PV.DATE]
    
    def __init__(self):
        super().__init__()
        self.date_text = ''
        self.keyword = 'before'
    
    def to_text(self) -> str:
        return f'{self.keyword} {self.date_text}'