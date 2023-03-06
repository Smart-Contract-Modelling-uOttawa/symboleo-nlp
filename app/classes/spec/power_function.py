from enum import Enum
from app.classes.spec.proposition import Proposition

class PowerFunction(Proposition):
    def to_sym(self):
        raise NotImplementedError()

class PFObligationName(Enum):
    Suspended = 'Suspended'
    Resumed = 'Resumed'
    Discharged = 'Discharged'
    Terminated = 'Terminated'
    Triggered = 'Triggered'

class PFObligation(PowerFunction):
    def __init__(self, name:PFObligationName, obligation_id: str):
        self.name = name
        self.norm = obligation_id

    def to_sym(self):
        return f'{self.name.value}(obligations.{self.norm})'


class PFContractName(Enum):
    Suspended = 'Suspended'
    Resumed = 'Resumed'
    Terminated = 'Terminated'

class PFContract(PowerFunction):
    def __init__(self, name:PFContractName):
        self.name = name

    def to_sym(self):
        return f'{self.name.value}(self)'
