from typing import List
from app.classes.patterns.pattern_classes import PatternClass
from app.classes.spec.norm import Norm
from app.classes.operations.handle_object import HandleObject

class IHandleNormUpdates:
    def handle(self, pattern_class: PatternClass, handle_object: HandleObject) -> List[Norm]:
        raise NotImplementedError()
