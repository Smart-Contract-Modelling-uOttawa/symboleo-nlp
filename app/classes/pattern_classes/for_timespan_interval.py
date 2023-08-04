from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV
from app.classes.spec.point_function import TimeUnit

class ForTimespanInterval(PatternClass):
    sequence = [PV.FOR_TIMESPAN, PV.AFTER_TIMEPOINT]

    # def __init__(self) -> None:
    #     super().__init__()
    #     self.keyword1 = ''
    #     self.timespan_unit: TimeUnit = None
    #     self.timespan_value = ''
    #     self.keyword2 = ''
    #     self.timepoint = ''
    
    # def to_text(self) -> str:
    #     return f'{self.keyword1} {self.timespan_value} {self.timespan_unit} {self.keyword2} {self.timepoint}'
    