from typing import List
from app.classes.frames.frame import Frame
from app.classes.spec.norm import Norm
from app.src.update_processor.pattern_handlers.handle_object import HandleObject

class IHandlePatterns:
    def handle(self, rame: Frame, handle_object: HandleObject) -> List[Norm]:
        raise NotImplementedError()
