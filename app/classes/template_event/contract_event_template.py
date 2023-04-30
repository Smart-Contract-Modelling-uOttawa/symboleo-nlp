from app.classes.template_event.templated_event import TemplatedEvent
from app.classes.custom_event.conj_type import ConjType
from app.classes.custom_event.verb import Verb

# Kill?
class ContractEventTemplate(TemplatedEvent):
    contract_verb: Verb 

    def to_text(self, conj_type: ConjType): # Need conjugation info
        if conj_type == ConjType.PRESENT:
            return f'contract {self.contract_verb.conjugations.present_plural}'
        elif conj_type == ConjType.CONTINUOUS:
            return f'contract {self.contract_verb.conjugations.continuous}'