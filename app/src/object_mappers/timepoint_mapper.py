from app.classes.spec.sym_event import SymEvent, VariableEvent, ContractEvent, ContractEventName

class IMapTimepoint:
    def map(self, evt: SymEvent) -> str:
        raise NotImplementedError()

class TimepointMapper(IMapTimepoint):
    def __init__(self):
        self.__contract_event_dict = {
            ContractEventName.Activated: 'self.start',
            ContractEventName.Terminated: 'self.end',
        }


    def map(self, evt: SymEvent) -> str:
        if isinstance(evt, VariableEvent):
            timepoint = f'{evt.name}.start'
        elif isinstance(evt, ContractEvent):
            timepoint = self.__contract_event_dict[evt.event_name]
        else:
            raise ValueError('Invalid Timepoint event')

        return timepoint


        