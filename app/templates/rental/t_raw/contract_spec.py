from typing import Dict
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.classes.events.custom_event.verb import Verb, VerbType, VerbConjugations
from app.classes.events.custom_event.prep_phrase import PrepPhrase
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import DeclarationProp, RoleDeclaration, AssetDeclaration, EventDeclaration
from app.classes.spec.norm import Obligation, Power
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.sym_event import ObligationEvent, ObligationEventName, ContractEvent, ContractEventName
from app.classes.spec.contract_spec_parameter import ContractSpecParameter as Parm
from app.classes.spec.other_predicates import *

arg_values = {
    #  'renter_id': 'renter',
    #  'landlord_id': 'landlord',
     'property_address': '[PROPERTY_ADDRESS]',
    #  'rent_amount': 1500,
     'currency': '[CURRENCY]',
     'extra_amount': '[EXTRA_AMOUNT]',
     'deposit_amount': '[DEPOSIT_AMOUNT]'
}

def get_contract_spec(arg_dict: Dict[str,str] = arg_values):
    parameters = [
        # Parm('renter_id', 'String'),
        # Parm('landlord_id', 'String'),
        Parm('property_address', 'String'),
        Parm('currency', 'Currency'),
        Parm('extra_amount', 'Number'),
        Parm('deposit_amount', 'Number')
    ]

    # Declarations
    renter = RoleDeclaration('renter', 'Renter')
    landlord = RoleDeclaration('landlord', 'Landlord')
    RENTER = renter.to_obj()
    LANDLORD = landlord.to_obj()

    the_property = AssetDeclaration('property', 'RentalProperty', [
        DeclarationProp('address', f'"{arg_dict["property_address"]}"','String')
    ])
    security_deposit = AssetDeclaration('security_deposit', 'SecurityDeposit', [
        DeclarationProp('amount', arg_dict["deposit_amount"], 'Number'),
        DeclarationProp('currency', f'Currency({arg_dict["currency"]})', 'Currency'),
    ],
    id='security_deposit')

    PROPERTY = the_property.to_obj()
    SECURITY_DEPOSIT = security_deposit.to_obj()

    evt_pay_deposit = EventDeclaration('evt_pay_deposit', 'PayDeposit', 
        [
            DeclarationProp('deposit', SECURITY_DEPOSIT, 'Number'),
            DeclarationProp('from', RENTER, 'Role'),
            DeclarationProp('to', LANDLORD, 'Role'),
        ]
    )

    evt_pay_extra = EventDeclaration('evt_pay_extra', 'PayAmount', [
        DeclarationProp('amount', arg_dict["extra_amount"], 'Number'),
        DeclarationProp('currency', f'Currency({arg_dict["currency"]})', 'Currency'),
        DeclarationProp('from', RENTER, 'Role'),
        DeclarationProp('to', LANDLORD, 'Role'),
    ])

    evt_occupy_property = EventDeclaration('evt_occupy_property', 'OccupyProperty', [
        DeclarationProp('agent', RENTER, 'Role'),
        DeclarationProp('property', PROPERTY, 'RentalProperty'),
    ])

    evt_keep_pet = EventDeclaration('evt_keep_pet', 'KeepPet', [
        DeclarationProp('agent', RENTER, 'Role')
    ])
    
    evt_allow_pets = EventDeclaration('evt_allow_pets', 'AllowPets', [
        DeclarationProp('grantor', LANDLORD, 'Role')
    ])

    # Variables to use
    EVT_PAY_EXTRA = evt_pay_extra.to_obj()
    EVT_PAY_DEPOSIT = evt_pay_deposit.to_obj()
    EVT_OCCUPY_PROPERTY = evt_occupy_property.to_obj()
    EVT_KEEP_PET = evt_keep_pet.to_obj()
    EVT_ALLOW_PETS = evt_allow_pets.to_obj()
    
    declarations = {
        'renter': renter,
        'landlord': landlord,
        'property': the_property,
        'security_deposit': security_deposit,
        'evt_pay_extra': evt_pay_extra,
        'evt_pay_deposit': evt_pay_deposit,
        'evt_occupy_property': evt_occupy_property,
        'evt_keep_pet': evt_keep_pet,
        'evt_allow_pets': evt_allow_pets
    }


    # Contract Spec
    contract_spec = ContractSpec(
        'rental',
        parameters = parameters,
        declarations = declarations,
        obligations = {
            'ob_pay_deposit': Obligation(
                'ob_pay_deposit',
                None,
                RENTER,
                LANDLORD,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionWHappensBeforeEvent(EVT_PAY_DEPOSIT, EVT_OCCUPY_PROPERTY)
                )
            ),
            'ob_pay_extra': Obligation(
                'ob_pay_extra',
                None,
                RENTER,
                LANDLORD,
                PropMaker.make(
                    PredicateFunctionHappens(ObligationEvent(ObligationEventName.Violated, 'ob_pay_deposit')) 
                ),
                PropMaker.make(PredicateFunctionHappens(EVT_PAY_EXTRA))
            ),
            'ob_no_pets': Obligation(
                'ob_no_pets',
                None,
                RENTER,
                LANDLORD,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_KEEP_PET),
                    negation=True
                )
            ),
        },
        
        powers = {
            'pow_terminate_ob_no_pets': Power(
                'pow_terminate_ob_no_pets',
                PropMaker.make(PredicateFunctionHappens(EVT_ALLOW_PETS)),
                LANDLORD,
                RENTER,
                PropMaker.make_default(),
                PFObligation(PFObligationName.Terminated, 'ob_no_pets')
            )
        }
    )

    return contract_spec
