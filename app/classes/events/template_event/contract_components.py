from app.classes.spec.sym_event import ContractEventName
from app.classes.events.custom_event.verb import Verb, VerbType, VerbConjugations
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.events.custom_event.noun_phrase import NounPhrase


class ContractNouns:
    contract = lambda: NounPhrase('contract', 'contract', asset_type='Contract')

class ContractVerbs:
    
    terminated = lambda: Verb('terminate', 'terminate', VerbType.INTRANSITIVE, VerbConjugations('terminate', 'terminates', 'terminated', 'terminating'))
    
    activated = lambda: Verb('activate', 'activate', VerbType.INTRANSITIVE, VerbConjugations('activate', 'activates', 'activated', 'activating'))

    verb_dict = {
        ContractEventName.Terminated: terminated,
        ContractEventName.Activated: activated
    }


class ContractEvents:
    def contract_event(c_event: ContractEventName):
        return CustomEvent(
            subj = ContractNouns.contract(),
            verb = ContractVerbs.verb_dict[c_event](),
            is_new = False
        )



class HelperVerbs:
    verb_is = lambda: Verb('is', 'be', VerbType.LINKING, VerbConjugations('is', 'are', 'was', 'is'))
    
    