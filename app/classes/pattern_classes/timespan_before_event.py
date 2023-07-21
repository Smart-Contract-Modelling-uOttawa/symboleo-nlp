from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV
from app.classes.spec.point_function import TimeUnit

class TimespanBeforeEvent(EventPatternClass):
    sequence = [PV.TIMESPAN, PV.P_BEFORE_T, PV.EVENT]

    def __init__(self) -> None:
        super().__init__()
        self.timespan_unit: TimeUnit = None
        self.timespan_value = ''
    
    def to_text(self) -> str:
        return f'{self.timespan_value} {self.timespan_unit.value} {self.keyword} {self.nl_event.to_text()}'

