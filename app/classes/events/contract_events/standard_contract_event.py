from app.classes.events.base_event import BaseEvent
from app.classes.events.conj_type import ConjType
from app.classes.spec.sym_event import ContractEvent, ContractEventName

class StandardContractEvent(BaseEvent):
    def __init__(self, action: str):
        self.action = action
    
    def to_sym_event(self):
        return ContractEvent(ContractEventName[self.action.capitalize()])

    def to_text(conj_type: ConjType = ConjType.CONTINUOUS) -> str:
        return super().to_text()

    def is_complete() -> bool:
        return super().is_complete()