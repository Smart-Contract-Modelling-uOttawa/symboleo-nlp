from app.classes.spec.sym_event import ContractEventName
from app.classes.custom_event.verb import Verb, VerbType, VerbConjugations
from app.classes.custom_event.noun_phrase import NounPhrase


class ContractNouns:
    contract = lambda: NounPhrase('contract', 'contract')

# TODO: Finish this 
class ContractVerbs:
    contract_verb_dict = {
        ContractEventName.Terminated: 
            lambda: Verb('terminated', 'terminate', [VerbType.INTRANSITIVE], VerbConjugations('terminate', 'terminates', 'terminated', 'terminating')),
        ContractEventName.Activated: 
            lambda: Verb('activated', 'activate', [VerbType.INTRANSITIVE], VerbConjugations('activate', 'activated', 'activated', 'activating')),
    }

    