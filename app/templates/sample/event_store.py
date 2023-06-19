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
    renter = lambda: NounPhrase('renter', 'renter', is_role=True, asset_type='Role')
    landlord = lambda: NounPhrase('landlord', 'landlord', is_role=True, asset_type='Role')


class EventStore:
    def pay(amount:str, curr, target_role):
        return CustomEvent(
            subj = SubjectStore.renter(),
            verb = VerbStore.pay(),
            dobj = NounPhrase(target_role, target_role, is_role=True, asset_type='Role'),
            # dobj = NounPhrase(amount, amount, asset_type='Money'),
            # pps= [
            #     PrepPhrase(f'to {target_role}', 'to', 
            #         NounPhrase(target_role, target_role, is_role=True, asset_type='Role'),
            #     ),
            #     PrepPhrase(f'in {curr}', 'in', 
            #         NounPhrase(curr, curr, asset_type='Currency'),
            #     )
            # ]
        )