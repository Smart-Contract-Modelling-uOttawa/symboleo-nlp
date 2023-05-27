from typing import List, Dict
from app.classes.spec.norm import Norm
from app.classes.patterns.pattern import Pattern

from app.src.update_processor.pattern_handlers.handle_object import HandleObject
from app.src.update_processor.pattern_handlers.pattern_handler import IHandlePatterns

class IExtractNormUpdates:
    def extract(self, pattern: Pattern, handle_object: HandleObject) -> List[Norm]:
        raise NotImplementedError()
    

# Here's the tough part
## What do we need for this?
## We want a common updater signature
## Might include: full contract, norm spec, NEW domain objects 

# Pattern will refer to some key (e.g. BEFORE_EVENT)
class NormUpdateExtractor(IExtractNormUpdates):
    def __init__(
        self, 
        handler_dict: Dict[str, IHandlePatterns]
    ):
        self.__handler_dict = handler_dict

    def extract(self, pattern: Pattern,  handle_object: HandleObject) -> List[Norm]:
        handler = self.__handler_dict[type(pattern)]
        norms = handler.handle(pattern, handle_object)
        return norms
        