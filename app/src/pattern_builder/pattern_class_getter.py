from typing import List
from app.classes.patterns.pattern_classes import *


class IGetAllPatternClasses:
    def get(self) -> List[PatternClass]:
        raise NotImplementedError()
    
class AllPatternClassGetter(IGetAllPatternClasses):
    def get(self) -> List[PatternClass]:
        return [
            BeforeDate(),
            BeforeEvent(),
            WithinTimespanEvent(),
            IfEvent()
        ]
    
    