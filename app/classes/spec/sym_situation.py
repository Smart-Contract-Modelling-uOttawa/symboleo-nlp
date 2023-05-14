from __future__ import annotations
from enum import Enum

class SymSituation:
    def to_sym(self):
        raise NotImplementedError()


class ObligationStateName(Enum):
    Create = 'Create'
    Discharge = 'Discharge'
    Active = 'Active'
    InEffect = 'InEffect'
    Suspension = 'Suspension'
    Violation = 'Violation'
    Fulfillment = 'Fulfillment'
    UnsuccessfulTermination = 'UnsuccessfulTermination'

class ObligationState(SymSituation):
    def __init__(self, state_name:ObligationStateName, obligation_variable:str):
        self.state_name = state_name
        self.obligation_variable = obligation_variable
    
    def __eq__(self, other: ObligationState) -> bool:
        return self.state_name == other.state_name and self.obligation_variable and other.obligation_variable
    
    def to_sym(self):
        return f'{self.state_name.value}(obligations.{self.obligation_variable})'


class PowerStateName(Enum):
    Create = 'Create'
    UnsuccessfulTermination = 'UnsuccessfulTermination'
    Active = 'Active'
    InEffect = 'InEffect'
    Suspension = 'Suspension'
    SuccessfulTermination = 'SuccessfulTermination'

class PowerState(SymSituation):
    def __init__(self, state_name:PowerStateName, power_variable: str):
        self.state_name = state_name
        self.power_variable = power_variable
    
    def __eq__(self, other: PowerState) -> bool:
        return self.state_name == other.state_name and self.power_variable and other.power_variable
    
    def to_sym(self):
        return f'{self.state_name.value}(powers.{self.power_variable})'


class ContractStateName(Enum):
    Form = 'Form'
    UnAssign = 'UnAssign'
    InEffect = 'InEffect'
    Suspension = 'Suspension'
    Rescission = 'Rescission'
    SuccessfulTermination = 'SuccessfulTermination'
    UnsuccessfulTermination = 'UnsuccessfulTermination'
    Active = 'Active'

class ContractState(SymSituation):
    def __init__(self, state_name: ContractStateName):
        self.state_name = state_name
    
    def __eq__(self, other: ContractState) -> bool:
        return self.state_name == other.state_name

    def to_sym(self):
        return f'{self.state_name.value}(self)'
    

