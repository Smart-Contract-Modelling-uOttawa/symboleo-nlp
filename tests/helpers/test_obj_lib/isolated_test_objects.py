from app.classes.spec.domain_object import Asset
from app.classes.spec.declaration import Declaration
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.classes.events.custom_event.prep_phrase import PrepPhrase
from app.classes.events.custom_event.verb import Verb, VerbConjugations, VerbType
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.events.custom_event.predicate import Predicate
from app.classes.events.custom_event.adverb import Adverb

class NounPhrases:
    # dolphin
    dolphin = lambda: NounPhrase('Dolphin', 'Dolphin', False, True, asset_type='Role')
    photos = lambda: NounPhrase('the original digital photo files', 'files', True, False, 'the', ['original', 'digital', 'photo'], 'Files')

    # cisco
    cisco = lambda: NounPhrase('cisco', 'cisco', is_role=True, asset_type='Role')
    distributor = lambda: NounPhrase('distributor', 'distributor', is_role=True, asset_type='Role')
    product = lambda: NounPhrase('any product', 'product', det='any', asset_type='Product')

    # porex
    porex = lambda: NounPhrase('Porex', 'Porex', is_role=True, asset_type='Role')
    cerus = lambda: NounPhrase('Cerus', 'Cerus', is_role=True, asset_type='Role')
    receipt = lambda: NounPhrase('invoice receipt', 'receipt', adjs=['invoice'], asset_type='Receipt')

    # tianhe
    sponsor = lambda: NounPhrase('Sponsor', 'Sponsor', is_role=True, asset_type='Role')
    stadium = lambda: NounPhrase('Stadium', 'Stadium', is_role=True, asset_type='Role')
    party = lambda: NounPhrase('the party', 'party', det='the', asset_type='Party')

    # prime
    prime = lambda: NounPhrase('Prime', 'Prime', is_role=True, asset_type='Role')
    shareholder = lambda: NounPhrase('Shareholder', 'Shareholder', is_role=True, asset_type='Role')
    components = lambda: NounPhrase('all project components', 'components', is_plural=True, det='all', adjs=['project'], asset_type='Components')

    # except_event
    partyA = lambda: NounPhrase('partyA', 'partyA', is_role=True, asset_type='Role')
    partyB = lambda: NounPhrase('partyB', 'partyB', is_role=True, asset_type='Role')
    approval = lambda: NounPhrase('approval', 'approval', asset_type='Approval')

    def date_np(date_str):
        return NounPhrase(date_str, date_str, asset_type='Date')

class Verbs:
    # cisco
    return_verb = lambda: Verb('returns', 'return', [VerbType.TRANSITIVE], VerbConjugations('return', 'returns', 'returned', 'returning') )
    
    # porex
    submit = lambda: Verb('submits', 'submit', [VerbType.TRANSITIVE], VerbConjugations('submit', 'submits', 'submitted', 'submitting'))

    # tianhe
    happening = lambda: Verb('happening', 'happen', [VerbType.INTRANSITIVE], VerbConjugations('happen', 'happens', 'happened', 'happening'))

    # prime
    completes = lambda: Verb('completes', 'complete', [VerbType.TRANSITIVE], VerbConjugations('complete', 'completes', 'completed', 'completing'))

    # except_event
    provides = lambda: Verb('provides', 'provide', [VerbType.TRANSITIVE], VerbConjugations('provide', 'provides', 'provided', 'providing'))

class CustomEvents:
    # cisco
    return_product = lambda: CustomEvent(
        subj = NounPhrases.distributor(),
        verb = Verbs.return_verb(),
        dobj = NounPhrases.product(),
        pps = [
            PrepPhrase('to cisco', 'to', NounPhrases.cisco())
        ]
    )

    # porex
    submit_receipt = lambda: CustomEvent(
        subj = NounPhrases.porex(),
        verb = Verbs.submit(),
        dobj = NounPhrases.receipt(),
        pps = [
            PrepPhrase('to Cerus', 'to', NounPhrases.cerus())
        ]
    )

    # tianhe
    party_happening = lambda: CustomEvent(
        subj = NounPhrases.party(),
        verb = Verbs.happening()   
    )

    # prime
    completes_components = lambda: CustomEvent(
        subj = NounPhrases.prime(),
        verb = Verbs.completes(),
        dobj = NounPhrases.components()
    )

    # except_event
    provides_approval = lambda: CustomEvent(
        subj = NounPhrases.partyA(),
        verb = Verbs.provides(),
        dobj = NounPhrases.approval()
    )
