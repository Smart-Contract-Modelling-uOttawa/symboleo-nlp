from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV
from app.classes.helpers.string_to_class import CaseConverter
from app.classes.operations.time_period import TimePeriod

class IMapTimePeriod:
    def map(self, pattern_class: PatternClass) -> TimePeriod:
        raise NotImplementedError()

class TimePeriodMapper(IMapTimePeriod):
    def __init__(self):
        self.__dict = TimePeriod.time_period_dict()

    def map(self, pattern_class: PatternClass) -> TimePeriod:
        if PV.TIME_PERIOD in pattern_class.val_dict:
            tpv = pattern_class.val_dict[PV.TIME_PERIOD]

            if tpv in self.__dict:
                return TimePeriod(self.__dict[tpv])
            else:
                return TimePeriod(CaseConverter.to_snake(tpv))

        else:
            raise ValueError('Pattern class is missing time period')


        