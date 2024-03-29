from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV
from app.classes.helpers.case_converter import CaseConverter
from app.classes.operations.time_period import TimePeriod

class IMapTimePeriod:
    def map(self, pattern_class: PatternClass) -> TimePeriod:
        raise NotImplementedError()

class TimePeriodMapper(IMapTimePeriod):
    def __init__(self):
        self.__dict = TimePeriod.time_period_dict()

    def map(self, pattern_class: PatternClass) -> TimePeriod:
        tpv = pattern_class.val_dict[PV.TIME_PERIOD]

        if tpv in self.__dict:
            return self.__dict[tpv]
        else:
            return TimePeriod(CaseConverter.to_snake(tpv))


        