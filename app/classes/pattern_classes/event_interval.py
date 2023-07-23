from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV

# TODO: Need to actually break this up into a few different ones
## Between Interval (between T1 and T2)
## From T1 until T2
## During Time period
## for Timespan following T
class EventInterval(PatternClass):
    sequence = [PV.INTERVAL]

    def __init__(self) -> None:
        super().__init__()
        self.keyword1 = ''
        self.keyword2 = ''
    
    def to_text(self) -> str:
        return f'{self.keyword1()} {self.nl_event.to_text()},'
    