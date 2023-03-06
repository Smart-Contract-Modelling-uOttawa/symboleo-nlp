from enum import Enum

class SymEvent:
    def to_sym(self):
        raise NotImplementedError()

# Note: I am trying to get rid of the VariableDotExpression in favour of specific dot expressions for each type
## e.g. a VariableEvent, VarriablePoint, etc
## This will keep the graph much cleaner, and should have no other impact
class VariableEvent(SymEvent):
    def __init__(self, name: str):
        self.name = name

    def to_sym(self):
        return f'{self.name}'

class PowerEventName(Enum):
    Triggered = 'Triggered'
    Activated = 'Activated'
    Suspended = 'Suspended'
    Resumed = 'Resumed'
    Exerted = 'Exerted'
    Expired = 'Expired'
    Terminated = 'Terminated'

class PowerEvent(SymEvent):
    def __init__(self, event_name: PowerEventName = PowerEventName.Activated, power_variable: str = ''):
        self.event_name = event_name
        self.power_variable = power_variable

    def __eq__(self, other):
        if (isinstance(other, PowerEvent)):
            return self.event_name == other.event_name and \
                   self.power_variable == other.power_variable
        return False

    def to_sym(self):
        return f'{self.event_name.value}(powers.{self.power_variable})'


class ObligationEventName(Enum):
    Triggered = 'Triggered'
    Activated = 'Activated'
    Suspended = 'Suspended'
    Resumed = 'Resumed'
    Discharged = 'Exerted'
    Expired = 'Expired'
    Fulfilled = 'Fulfilled'
    Violated = 'Violated'
    Terminated = 'Terminated'

class ObligationEvent(SymEvent):
    def __init__(self, event_name: ObligationEventName = ObligationEventName.Activated, obligation_variable: str = ''):
        self.event_name = event_name
        self.obligation_variable = obligation_variable

    def __eq__(self, other):
        if (isinstance(other, ObligationEvent)):
            return self.event_name == other.event_name and \
                   self.obligation_variable == other.obligation_variable
        return False

    def to_sym(self):
        return f'{self.event_name.value}(obligations.{self.obligation_variable})'


class ContractEventName(Enum):
    Activated = 'Activated'
    Suspended = 'Suspended'
    Resumed = 'Resumed'
    FulfilledObligations = 'FulfilledObligations'
    RevokedParty = 'RevokedParty'
    AssignedParty = 'AssignedParty'
    Terminated = 'Terminated'
    Rescinded = 'Rescinded'

class ContractEvent(SymEvent):
    def __init__(self, event_name: ContractEventName = ContractEventName.Activated):
        self.event_name = event_name

    def __eq__(self, other):
        if (isinstance(other, ContractEvent)):
            return self.event_name == other.event_name
        return False

    def to_sym(self):
        return f'{self.event_name.value}(self)'
