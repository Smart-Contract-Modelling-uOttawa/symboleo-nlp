from app.classes.spec.domain_object import Asset
from app.classes.spec.declaration import Declaration
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.classes.events.custom_event.prep_phrase import PrepPhrase
from app.classes.events.custom_event.verb import Verb, VerbConjugations, VerbType
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.events.custom_event.predicate import Predicate
from app.classes.events.custom_event.adverb import Adverb

from app.classes.events.custom_event.verb_store import VerbStore

class SubjectStore:
    contractor = lambda: NounPhrase('contractor', 'contractor', is_role=True, asset_type='Role')
    client = lambda: NounPhrase('client', 'client', is_role=True, asset_type='Role')


class EventStore:
    def pay(target_role='contractor'):
        return CustomEvent(
            subj = SubjectStore.client(),
            verb = VerbStore.pay(),
            dobj = NounPhrase('money', 'money', asset_type='Money'),
            pps= [
                PrepPhrase(f'to {target_role}', 'to', 
                    NounPhrase(target_role, target_role, is_role=True, asset_type='Role'),
                )
            ],
            event_key='evt_pay'
        )