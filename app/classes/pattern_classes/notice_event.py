from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV


class NoticeEvent(EventPatternClass):
    sequence = [PV.CONDITIONAL_N, PV.TIMESPAN, PV.NOTICE_EVENT]

    def __init__(self) -> None:
        super().__init__()
    
    def to_text(self) -> str:
        return f'{self.keyword.capitalize()} {self.nl_event.to_text()},'
    