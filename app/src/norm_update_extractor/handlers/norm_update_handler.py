from typing import List
from app.classes.pattern_classes.pattern_class import PatternClass
from app.classes.spec.norm import Norm
from app.classes.spec.norm_config import NormConfig

class IHandleNormUpdates:
    def handle(self, pattern_class: PatternClass, norm_config: NormConfig) -> List[Norm]:
        raise NotImplementedError()
