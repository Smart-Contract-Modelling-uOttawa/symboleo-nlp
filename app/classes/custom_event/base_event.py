from app.classes.spec.sym_event import ContractEvent, ContractEventName, ObligationEvent, ObligationEventName

class BaseEvent:
    def to_sym_event(self):
        raise NotImplementedError()

class StandardContractEvent(BaseEvent):
    def __init__(self, action: str):
        self.action = action
    
    def to_sym_event(self):
        return ContractEvent(ContractEventName[self.action.capitalize()])

class StandardObligationEvent(BaseEvent):
    def __init__(self):
        self.ob_var: str = None
        self.action: str = None
    
    def to_sym_event(self):
        return ObligationEvent(ObligationEventName[self.action.capitalize()], self.ob_var)