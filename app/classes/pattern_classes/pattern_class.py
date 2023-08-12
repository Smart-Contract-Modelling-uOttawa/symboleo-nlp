from typing import List, Dict
from app.classes.pattern_classes.pattern_variables import PatternVariable

from app.classes.spec.sym_event import SymEvent, ContractEvent
from app.classes.events.custom_event.custom_event import CustomEvent, ConjType
from app.classes.events.template_event.contract_components import ContractVerbs

class PatternClass:
    sequence: List[PatternVariable] = []
    conj_type: ConjType = ConjType.BASIC

    def __init__(self, val_dict = None) -> None:
        self.keyword = ''
        self.val_dict: Dict[PatternVariable, str] = val_dict or {}

    def to_text(self) -> str:
        pv_list = [self.val_dict[x] for x in self.sequence]
        return ' '.join(pv_list)


class EventPatternClass(PatternClass):
    def __init__(self, val_dict = None) -> None:
        super().__init__(val_dict)
        self.event: SymEvent = None
        self.nl_event: CustomEvent = None

    def to_text(self) -> str:
        # If its a norm event, then replace with the nl_event...
        if isinstance(self.event, ContractEvent):
            self.val_dict[PatternVariable.EVENT] = self._contract_event(self.conj_type)
        
        return super().to_text()


    def _contract_event(self, conj_type: ConjType):
        evt: ContractEvent = self.event
        verb = ContractVerbs.verb_dict[evt.event_name]()

        if conj_type == ConjType.CONTINUOUS:
            return f'contract {verb.conjugations.continuous}'
        else:
            return f'contract {verb.conjugations.present_plural}'
