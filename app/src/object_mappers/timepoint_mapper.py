from app.classes.spec.sym_event import SymEvent, VariableEvent, ContractEvent, ContractEventName
from app.classes.spec.sym_point import PointExpression, PointVDE, PointAtomContractEvent

class IMapTimepoint:
    def map(self, evt: SymEvent) -> PointExpression:
        raise NotImplementedError()

class TimepointMapper(IMapTimepoint):

    def map(self, evt: SymEvent) -> PointExpression:
        if isinstance(evt, VariableEvent):
            timepoint = PointVDE(f'{evt.name}.start')
        elif isinstance(evt, ContractEvent):
            timepoint = PointAtomContractEvent(evt)
        else:
            raise ValueError('Invalid Timepoint event')

        return timepoint


        