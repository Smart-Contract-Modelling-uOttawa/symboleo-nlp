class PowerFunction:
    def to_sym(self):
        raise NotImplementedError()

class PFObligation(PowerFunction):
    def __init__(self, name:str, obligation_id: str):
        self.name = name #'Suspended', 'Resumed', 'Discharged', 'Terminated', 'Triggered'
        self.norm = obligation_id

    def to_sym(self):
        return f'{self.name}(obligations.{self.norm})'


class PFContract(PowerFunction):
    def __init__(self, name:str):
        self.name = name #'Suspended', 'Resumed', 'Terminated'

    def to_sym(self):
        return f'{self.name}(self)'
