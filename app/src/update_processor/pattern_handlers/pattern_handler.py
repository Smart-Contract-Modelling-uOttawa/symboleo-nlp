from typing import List
from app.classes.patterns.pattern import Pattern
from app.classes.spec.norm import Norm
from app.classes.operations.handle_object import HandleObject

class IHandlePatterns:
    def handle(self, pattern: Pattern, handle_object: HandleObject) -> List[Norm]:
        raise NotImplementedError()
