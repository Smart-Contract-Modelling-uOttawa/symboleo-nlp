class SymEvent:
    def to_sym(self):
        raise NotImplementedError()

class EventVDE:
    def __init__(self, name: str = ''):
        self.name = name
    
    def to_sym(self):
        return self.name

class VariableEvent(SymEvent):
    variable = EventVDE()
    
    def __init__(self, variable: EventVDE):
        self.variable = variable

    def to_sym(self):
        return f'{self.variable.to_sym()}'

# class VariableEvent(SymEvent):
#     variable = VariableDotExpression()
    
#     def __init__(self, variable: VariableDotExpression):
#         self.variable = variable

#     def to_sym(self):
#         return f'{self.variable.to_sym()}'


class PowerEvent(SymEvent):
    def __init__(self, event_name: str = '', power_variable: str = ''):
        self.event_name = event_name # 	'Triggered' | 'Activated' | 'Suspended' | 'Resumed' | 'Exerted' | 'Expired' | 'Terminated';
        self.power_variable = power_variable

    def __eq__(self, other):
        if (isinstance(other, PowerEvent)):
            return self.event_name == other.event_name and \
                   self.power_variable == other.power_variable
        return False

    def to_sym(self):
        return f'{self.event_name}(powers.{self.power_variable})'


class ObligationEvent(SymEvent):
    def __init__(self, event_name: str = '', obligation_variable: str = ''):
        self.event_name = event_name # 	'Triggered' | 'Activated' | 'Suspended' | 'Resumed' | 'Discharged' | 'Expired' | 'Fulfilled' | 'Violated' | 'Terminated';
        self.obligation_variable = obligation_variable

    def __eq__(self, other):
        if (isinstance(other, ObligationEvent)):
            return self.event_name == other.event_name and \
                   self.obligation_variable == other.obligation_variable
        return False

    def to_sym(self):
        return f'{self.event_name}(obligations.{self.obligation_variable})'


class ContractEvent(SymEvent):
    def __init__(self, event_name: str = ''):
        self.event_name = event_name # 	'Activated' | 'Suspended' | 'Resumed' | 'FulfilledObligations' | 'RevokedParty' | 'AssignedParty' | 'Terminated' | 'Rescinded';

    def __eq__(self, other):
        if (isinstance(other, ContractEvent)):
            return self.event_name == other.event_name
        return False

    def to_sym(self):
        return f'{self.event_name}(self)'
