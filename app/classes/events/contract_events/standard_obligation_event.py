from app.classes.events.base_event import BaseEvent
from app.classes.events.conj_type import ConjType
from app.classes.spec.sym_event import ObligationEvent, ObligationEventName

class StandardObligationEvent(BaseEvent):
    def __init__(self):
        self.ob_var: str = None
        self.action: str = None
    
    def to_sym_event(self):
        return ObligationEvent(ObligationEventName[self.action.capitalize()], self.ob_var)
    
    def to_text(conj_type: ConjType = ConjType.CONTINUOUS) -> str:
        return super().to_text()

    def is_complete() -> bool:
        return super().to_text()