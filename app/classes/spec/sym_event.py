from app.classes.spec.helpers import VariableDotExpression

class SymEvent:
    def to_sym(self):
        raise NotImplementedError()


class VariableEvent(SymEvent):
    variable = VariableDotExpression()
    
    def __init__(self, variable: VariableDotExpression):
        self.variable = variable

    def to_sym(self):
        return f'{self.variable.to_sym()}'


class PowerEvent(SymEvent):
    def __init__(self, event_name: str = '', power_variable: str = ''):
        self.event_name = event_name # 	'Triggered' | 'Activated' | 'Suspended' | 'Resumed' | 'Exerted' | 'Expired' | 'Terminated';
        self.power_variable = power_variable

    def to_sym(self):
        return f'{self.event_name}(powers.{self.power_variable})'


class ObligationEvent(SymEvent):
    def __init__(self, event_name: str = '', obligation_variable: str = ''):
        self.event_name = event_name # 	'Triggered' | 'Activated' | 'Suspended' | 'Resumed' | 'Discharged' | 'Expired' | 'Fulfilled' | 'Violated' | 'Terminated';
        self.obligation_variable = obligation_variable

    def to_sym(self):
        return f'{self.event_name}(obligations.{self.obligation_variable})'


class ContractEvent(SymEvent):
    def __init__(self, event_name: str = ''):
        self.event_name = event_name # 	'Activated' | 'Suspended' | 'Resumed' | 'FulfilledObligations' | 'RevokedParty' | 'AssignedParty' | 'Terminated' | 'Rescinded';

    def to_sym(self):
        return f'{self.event_name}(self)'
