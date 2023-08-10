from typing import List, Type
from app.classes.pattern_classes.pattern_class import PatternClass
from app.classes.pattern_classes.all_pattern_classes import *
from app.classes.spec.parameter_config import PatternClassType

class IGetAllPatternClasses:
    def get(self, config: List[PatternClassType] = None) -> List[Type[PatternClass]]:
        raise NotImplementedError()
    
class AllPatternClassGetter(IGetAllPatternClasses):
    def get(self, config: List[PatternClassType] = None) -> List[Type[PatternClass]]:
        # return [
        #     BeforeDate(),
        #     BeforeEvent(),
        #     WithinTimespanEvent(),
        #     CondAEvent(),
        #     CondTEvent(),
        #     ExceptEvent(),
        # ]
        result = []

        if not config or len(config) == 0:
            return get_all_pattern_classes()
        else:
            if PatternClassType.TEMPORAL in config:
                result.extend(temporal_classes())

                if PatternClassType.UNTIL in config:
                    result.extend(until_classes())

            if PatternClassType.CONDITIONAL in config:
                result.extend(conditional_classes())
            
            if PatternClassType.EXCEPTION in config:
                result.extend(exception_classes())
        
        return self._dedupe(result)

    def _dedupe(self, my_list: List[Type[PatternClass]]) -> List[Type[PatternClass]]:
        d_a: List[Type[PatternClass]] = []
        for x in my_list:
            if type(x) not in [type(y) for y in d_a]:
                d_a.append(x)
        return d_a

    
    
    