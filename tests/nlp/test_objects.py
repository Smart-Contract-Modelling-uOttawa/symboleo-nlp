from app.classes.spec.domain_object import Asset
from app.classes.spec.declaration import Declaration
from app.classes.other.noun_phrase import NounPhrase
from app.classes.other.prep_phrase import PrepPhrase
from app.classes.other.verb import Verb, VerbConjugations, VerbType
from app.classes.other.frame_event import FrameEvent
from app.classes.other.predicate import Predicate
from app.classes.other.adverb import Adverb

class NounPhrases:
    legal_proceedings = lambda: NounPhrase('legal proceedings', 'proceedings', is_plural=True, adjs=['legal'])
    credit_card = lambda: NounPhrase('credit card', 'card', adjs=['credit'])
    apple_pie =  lambda: NounPhrase('apple pie', 'pie', adjs=['apple'])
    pets =  lambda: NounPhrase('pets', 'pets', is_plural=True)
    the_seller = lambda: NounPhrase('the seller', 'seller', is_role=True, det = 'the')
    buyer = lambda: NounPhrase('buyer', 'buyer', is_role=True)
    hundred_dollars = lambda: NounPhrase('$100', '$100')
    legal_pro = lambda: NounPhrase('a legal professional', 'professional', det='a', adjs=['legal'])
    canada = lambda: NounPhrase('Canada', 'Canada')
    property = lambda: NounPhrase('property', 'property', det='the')
    bob = lambda: NounPhrase('Bob', 'Bob', is_role=True)

class Verbs:
    become = lambda: Verb('become', 'become', [VerbType.LINKING], VerbConjugations('become', 'becomes', 'became', 'becoming'))
    pays = lambda: Verb('pays', 'pay', [VerbType.TRANSITIVE], VerbConjugations('pay', 'pays', 'paid', 'paying'))
    buys = lambda: Verb('buys', 'buy', [VerbType.TRANSITIVE], VerbConjugations('buy', 'buys', 'bought', 'buying'))
    sues = lambda: Verb('sues', 'sue', [VerbType.TRANSITIVE], VerbConjugations('sue', 'sues', 'sued', 'suing'))
    eats = lambda: Verb('eats', 'eat', [VerbType.TRANSITIVE], VerbConjugations('eat', 'eats', 'ate', 'eating'))

class FrameEvents:
    legal_proceedings = lambda: FrameEvent(
        subj = NounPhrases.legal_proceedings(),
        verb = Verbs.become(),
        predicate = Predicate('necessary')
    )
    paying = lambda: FrameEvent(
        subj = NounPhrases.buyer(),
        verb = Verbs.pays(),
        dobj = NounPhrases.hundred_dollars(),
        pps = [ 
            PrepPhrase('to the seller', 'to', NounPhrases.the_seller()),
            PrepPhrase('with a credit card', 'with', NounPhrases.credit_card())
        ]
    )
    legal_pie = lambda: FrameEvent(
        subj = NounPhrases.legal_pro(),
        verb = Verbs.sues(),
        dobj = NounPhrases.the_seller(),
        pps = [
            PrepPhrase('for apple pie', 'for', NounPhrases.apple_pie()),
            PrepPhrase('in Canada', 'in', NounPhrases.canada())
        ]
    )
    legal_proceedings_det = lambda: FrameEvent(
        subj=NounPhrases.legal_proceedings(),
        verb=Verbs.become(),
        predicate=Predicate('necessary'),
        pps = [
            PrepPhrase('on the property', 'on', NounPhrases.property()),
            PrepPhrase('in Canada', 'in', NounPhrases.canada()),
        ]
    )
    eating_pie = lambda: FrameEvent(
        subj = NounPhrases.bob(),
        verb = Verbs.eats(),
        dobj = NounPhrases.apple_pie(),
        adverb = Adverb('noisily'),
        pps = [PrepPhrase('with the seller', 'with', NounPhrases.the_seller())]
    )

class Assets:
    legal_proceedings = lambda: Asset('LegalProceedings', [])
    amount = lambda: Asset('Amount', [])
    canada = lambda: Asset('Canada', [])
    property = lambda: Asset('Property', [])

class AssetDeclarations:
    legal_proceedings = lambda: Declaration('legal proceedings', 'LegalProceedings', 'assets', [])
    credit_card = lambda: Declaration('credit card', 'CreditCard', 'assets', []) # PaymentMethod...?
    pets = lambda: Declaration('pets', 'Pets', 'assets', []) # ??
    hundred_dollars = lambda: Declaration('$100', 'Amount', 'assets', [])
    canada = lambda: Declaration('Canada', 'Country', 'assets', [])
    property = lambda: Declaration('property', 'Property', 'assets', [])
