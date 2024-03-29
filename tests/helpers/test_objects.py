from app.classes.spec.domain_object import Asset
from app.classes.spec.declaration import RoleDeclaration, AssetDeclaration, EventDeclaration
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.classes.events.custom_event.prep_phrase import PrepPhrase
from app.classes.events.custom_event.verb import Verb, VerbConjugations, VerbType
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.events.custom_event.predicate import Predicate
from app.classes.events.custom_event.adverb import Adverb

class NounPhrases:
    # Roles
    the_seller = lambda: NounPhrase('the seller', 'seller', is_role=True, det = 'the', asset_type='Role', asset_id='seller')
    buyer = lambda: NounPhrase('buyer', 'buyer', is_role=True, asset_type='Role', asset_id='buyer')
    bob = lambda: NounPhrase('Bob', 'Bob', is_role=True, asset_type='Role', asset_id='bob')
    renter = lambda: NounPhrase('renter', 'renter', is_role=True, asset_type='Role', asset_id='renter')
    client = lambda: NounPhrase('client', 'client', False, True, asset_type='Role')
    contractor = lambda: NounPhrase('contractor', 'contractor', False, True, asset_type='Role')
    landlord = lambda: NounPhrase('landlord', 'landlord', is_role=True, asset_type='Role')


    legal_proceedings = lambda: NounPhrase('legal proceedings', 'proceedings', is_plural=True, adjs=['legal'], asset_type='Proceedings')
    credit_card = lambda: NounPhrase('credit card', 'card', adjs=['credit'], asset_type='PaymentMethod')
    apple_pie =  lambda: NounPhrase('apple pie', 'pie', adjs=['apple'], asset_type='Pie')
    pets =  lambda: NounPhrase('pets', 'pets', is_plural=True, asset_type='Pets')
    hundred_dollars = lambda: NounPhrase('$100', '100', asset_type='Money')
    legal_pro = lambda: NounPhrase('a legal professional', 'professional', det='a', adjs=['legal'], asset_type='Professional')
    canada = lambda: NounPhrase('Canada', 'Canada', asset_type='Location')
    property = lambda: NounPhrase('property', 'property', asset_type='RentalProperty')
    cad = lambda: NounPhrase('CAD', 'CAD', False, False, asset_type='Currency')
    test_value_parm = lambda: NounPhrase('[TEST_VALUE]', '[TEST_VALUE]', is_parm=True, asset_type='String')
    services = lambda: NounPhrase('services', 'services', True, False, asset_type='Services')
    disclosure = lambda: NounPhrase('disclosure', 'disclosure', False, False, asset_type='Disclosure')
    client_cap = lambda: NounPhrase('CLIENT', 'CLIENT', False, True, asset_type='Role')
    bosch = lambda: NounPhrase('BOSCH', 'BOSCH', False, True, asset_type='Role')
    productivity = lambda: NounPhrase('productivity', 'productivity', False, False, asset_type='Productivity')

    authorization = lambda: NounPhrase('authorization', 'authorization', asset_type='Authorization')
    phone = lambda: NounPhrase('the phone', 'phone', False, False, 'the', asset_type='Phone')
    contract = lambda: NounPhrase('contract', 'contract', asset_type='Contract')

    def date_np(date_str):
        return NounPhrase(date_str, date_str, asset_type='Date')

class Verbs:
    become = lambda: Verb('become', 'become', VerbType.LINKING, VerbConjugations('become', 'becomes', 'became', 'becoming'))
    pays = lambda: Verb('pays', 'pay', VerbType.TRANSITIVE, VerbConjugations('pay', 'pays', 'paid', 'paying'))
    buys = lambda: Verb('buys', 'buy', VerbType.TRANSITIVE, VerbConjugations('buy', 'buys', 'bought', 'buying'))
    sues = lambda: Verb('sues', 'sue', VerbType.TRANSITIVE, VerbConjugations('sue', 'sues', 'sued', 'suing'))
    eats = lambda: Verb('eats', 'eat', VerbType.TRANSITIVE, VerbConjugations('eat', 'eats', 'ate', 'eating'))
    abandons = lambda: Verb('abandons', 'abandon', VerbType.TRANSITIVE, VerbConjugations('abandon', 'abandons', 'abandonned', 'abandonning'))
    occupies = lambda: Verb('occupies', 'occupy', VerbType.TRANSITIVE, VerbConjugations('occupy', 'occupies', 'occupied', 'occupying'))
    disrupts = lambda: Verb('disrupts', 'disrupt', VerbType.TRANSITIVE, VerbConjugations('disrupt', 'disrupts', 'disrupted', 'disrupting'))
    provides = lambda: Verb('provides', 'provide', VerbType.TRANSITIVE, VerbConjugations('provide', 'provides', 'provided', 'providing'))
    complies = lambda: Verb('complies', 'comply', VerbType.INTRANSITIVE, VerbConjugations('comply', 'complies', 'complied', 'complying'))


class CustomEvents:
    legal_proceedings = lambda: CustomEvent(
        subj = NounPhrases.legal_proceedings(),
        verb = Verbs.become(),
        predicate = Predicate('necessary')
    )
    paying = lambda: CustomEvent(
        subj = NounPhrases.buyer(),
        verb = Verbs.pays(),
        dobj = NounPhrases.hundred_dollars(),
        pps = [ 
            PrepPhrase('to the seller', 'to', NounPhrases.the_seller()),
            PrepPhrase('with a credit card', 'with', NounPhrases.credit_card())
        ]
    )
    legal_pie = lambda: CustomEvent(
        subj = NounPhrases.legal_pro(),
        verb = Verbs.sues(),
        dobj = NounPhrases.the_seller(),
        pps = [
            PrepPhrase('for apple pie', 'for', NounPhrases.apple_pie()),
            PrepPhrase('in Canada', 'in', NounPhrases.canada())
        ]
    )
    legal_proceedings_det = lambda: CustomEvent(
        subj=NounPhrases.legal_proceedings(),
        verb=Verbs.become(),
        predicate=Predicate('necessary'),
        pps = [
            PrepPhrase('on the property', 'on', NounPhrases.property()),
            PrepPhrase('in Canada', 'in', NounPhrases.canada()),
        ]
    )
    eating_pie = lambda: CustomEvent(
        subj = NounPhrases.bob(),
        verb = Verbs.eats(),
        dobj = NounPhrases.apple_pie(),
        adverb = Adverb('noisily'),
        pps = [PrepPhrase('with the seller', 'with', NounPhrases.the_seller())]
    )
    eating_parm = lambda: CustomEvent(
        subj = NounPhrases.bob(),
        verb = Verbs.eats(),
        dobj = NounPhrases.test_value_parm()
    )
    abandon_property = lambda: CustomEvent(
        subj = NounPhrases.renter(),
        verb = Verbs.abandons(),
        dobj = NounPhrases.property()
    )
    occupy_property = lambda: CustomEvent(
        subj = NounPhrases.renter(),
        verb = Verbs.occupies(),
        dobj = NounPhrases.property()
    )
    provide_authorization = lambda: CustomEvent(
        subj = NounPhrases.renter(),
        verb = Verbs.provides(),
        dobj = NounPhrases.authorization(),
        pps = [
            PrepPhrase('for pets', 'for', NounPhrases.pets())
        ]
    )
    disrupt_buyer = lambda: CustomEvent(
        subj = NounPhrases.bob(),
        verb = Verbs.disrupts(),
        dobj = NounPhrases.buyer(),
        pps = [
            PrepPhrase('on the phone', 'on', NounPhrases.phone())
        ]
    )
    contract_dobj = lambda: CustomEvent(
        subj = NounPhrases.bob(),
        verb = Verbs.buys(),
        dobj = NounPhrases.contract()
    )
    bob_complies = lambda: CustomEvent(
        subj = NounPhrases.bob(),
        verb = Verbs.complies(),
    )
    bob_happy = lambda: CustomEvent(
        subj = NounPhrases.bob(),
        verb = Verbs.become(),
        predicate = Predicate('happy')
    )
    


class Assets:
    legal_proceedings = lambda: Asset('LegalProceedings', [])
    amount = lambda: Asset('Amount', [])
    canada = lambda: Asset('Canada', [])
    property = lambda: Asset('Property', [])

class AssetDeclarations:
    legal_proceedings = lambda: AssetDeclaration('legal proceedings', 'LegalProceedings')
    credit_card = lambda: AssetDeclaration('credit card', 'CreditCard') # PaymentMethod...?
    pets = lambda: AssetDeclaration('pets', 'Pets') # ??
    hundred_dollars = lambda: AssetDeclaration('$100', 'Money')
    canada = lambda: AssetDeclaration('Canada', 'Country')
    property = lambda: AssetDeclaration('property', 'Property')
    pie = lambda: AssetDeclaration('apple_pie', 'Pie')
