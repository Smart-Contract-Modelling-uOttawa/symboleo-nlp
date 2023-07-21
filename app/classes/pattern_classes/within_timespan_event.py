from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV
from app.classes.spec.point_function import TimeUnit
from app.classes.events.conj_type import ConjType

class WithinTimespanEvent(EventPatternClass):
    sequence = [PV.WITHIN, PV.TIMESPAN, PV.P_AFTER_W, PV.EVENT]

    def __init__(self) -> None:
        super().__init__()
        self.timespan_unit: TimeUnit = None
        self.timespan_value = ''
    
    def to_text(self) -> str:
        return f'within {self.timespan_value} {self.timespan_unit.value} {self.keyword} {self.nl_event.to_text(ConjType.CONTINUOUS)}'

