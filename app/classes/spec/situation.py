class Situation:
    def to_sym(self):
        raise NotImplementedError()

class ObligationState(Situation):
    def __init__(self, state_name:str, obligation_variable:str):
        self.state_name = state_name # 	'Create' | 'Discharge' | 'Active' | 'InEffect' | 'Suspension' | 'Violation' | 'Fulfillment' | 'UnsuccessfulTermination';
        self.obligation_variable = obligation_variable
    
    def to_sym(self):
        return f'{self.state_name}(obligations.{self.obligation_variable})'

class PowerState(Situation):
    def __init__(self, state_name:str, power_variable: str):
        self.state_name = state_name # 	'Create' | 'UnsuccessfulTermination' | 'Active' | 'InEffect' | 'Suspension' | 'SuccessfulTermination';
        self.power_variable = power_variable
    
    def to_sym(self):
        return f'{self.state_name}(powers.{self.power_variable})'

class ContractState(Situation):
    def __init__(self, state_name:str):
        self.state_name = state_name # 	'Form' | 'UnAssign' | 'InEffect' | 'Suspension' | 'Rescission' | 'SuccessfulTermination' | 'UnsuccessfulTermination' | 'Active';
    
    def to_sym(self):
        return f'{self.state_name}(self)'
    

