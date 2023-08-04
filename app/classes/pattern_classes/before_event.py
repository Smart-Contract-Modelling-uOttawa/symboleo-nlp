from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class BeforeEvent(EventPatternClass):
    sequence = [PV.P_BEFORE_E, PV.EVENT]

    # def __init__(self) -> None:
    #     super().__init__()
    
    # def to_text(self) -> str:
    #     return f'{self.keyword} {self.nl_event.to_text()}'
    
