from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

# TODO: Need the timepoints
class EventInterval(EventPatternClass):
    sequence = [PV.EVENT, PV.INTERVAL]

    def __init__(self) -> None:
        super().__init__()
    
    def to_text(self) -> str:
        return f'{self.keyword.capitalize()} {self.nl_event.to_text()},'
    