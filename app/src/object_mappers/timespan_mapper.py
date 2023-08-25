from typing import Tuple
from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV
from app.classes.spec.point_function import TimeUnit

class IMapTimespan:
    def map(self, pattern_class: PatternClass) -> Tuple[str, TimeUnit]:
        raise NotImplementedError()

class TimespanMapper(IMapTimespan):

    def map(self, pattern_class: PatternClass) -> Tuple[str, TimeUnit]:
        timespan_str:str = pattern_class.val_dict[PV.TIMESPAN]
        tv, tu = timespan_str.split(' ')

        if tu.capitalize() in TimeUnit.__dict__:
            tu = TimeUnit[tu.capitalize()]
        
        # Singular case
        elif (tu + 's').capitalize() in TimeUnit.__dict__:
            tu = TimeUnit[(tu + 's').capitalize()]
        
        else:
            raise ValueError('Invalid Timespan')

        return (tv, tu)


        