from typing import List, Type
from app.classes.pattern_classes.pattern_class import PatternClass
from app.classes.pattern_classes.all_pattern_classes import *
from app.classes.spec.parameter_config import PatternClassType

class IGetAllPatternClasses:
    def get(self, config: List[PatternClassType] = None) -> List[Type[PatternClass]]:
        raise NotImplementedError()
    
class AllPatternClassGetter(IGetAllPatternClasses):
    def get(self, config: List[PatternClassType] = None) -> List[Type[PatternClass]]:

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
        
        return list(set(result))

    
    
    