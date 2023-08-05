from typing import List, Dict, Type
from app.classes.spec.norm import Norm
from app.classes.spec.norm_config import NormConfig
from app.classes.pattern_classes.pattern_class import PatternClass

from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates

class IExtractNormUpdates:
    def extract(self, pattern_class: PatternClass, norm_config: NormConfig) -> List[Norm]:
        raise NotImplementedError()
    
class NormUpdateExtractor(IExtractNormUpdates):
    def __init__(
        self, 
        handler_dict: Dict[Type, IHandleNormUpdates]
    ):
        self.__handler_dict = handler_dict

    def extract(self, pattern_class: PatternClass, norm_config: NormConfig) -> List[Norm]:
        handler = self.__handler_dict[type(pattern_class)]
        norms = handler.handle(pattern_class, norm_config)
        return norms
        