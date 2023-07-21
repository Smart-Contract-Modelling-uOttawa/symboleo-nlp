from typing import List
from app.classes.pattern_classes.pattern_class import PatternClass
from app.classes.pattern_classes.all_pattern_classes import *

class IGetAllPatternClasses:
    def get(self) -> List[PatternClass]:
        raise NotImplementedError()
    
class AllPatternClassGetter(IGetAllPatternClasses):
    def get(self) -> List[PatternClass]:
        # return [
        #     BeforeDate(),
        #     BeforeEvent(),
        #     WithinTimespanEvent(),
        #     CondAEvent(),
        #     CondTEvent(),
        #     ExceptEvent(),
        # ]
    
        return get_all_pattern_classes()
    
    
    