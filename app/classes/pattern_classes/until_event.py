from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class UntilEvent(EventPatternClass):
    sequence = [PV.UNTIL, PV.EVENT]
    
    def __init__(self):
        super().__init__()
    
    def to_text(self) -> str:
        return f'{self.keyword} {self.nl_event.to_text()}'