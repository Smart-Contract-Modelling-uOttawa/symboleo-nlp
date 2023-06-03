from app.classes.spec.sym_event import ContractEventName, ObligationEventName
from app.classes.events.custom_event.verb import Verb, VerbType, VerbConjugations
from app.classes.events.custom_event.noun_phrase import NounPhrase


class ContractNouns:
    contract = lambda: NounPhrase('contract', 'contract', asset_type='Contract')

# TODO: F1 - Finish this 
class ContractVerbs:
    contract_verb_dict = {
        'terminate': ContractEventName.Terminated,
        'begin': ContractEventName.Activated
    }


    


class HelperVerbs:
    verb_is = lambda: Verb('is', 'be', [VerbType.LINKING], VerbConjugations('is', 'are', 'was', 'is'))
    
    