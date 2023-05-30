from typing import Dict
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import DeclarationProp, RoleDeclaration, AssetDeclaration, EventDeclaration
from app.classes.spec.norm import Obligation, Power
from app.classes.spec.prop_maker import PropMaker
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.sym_event import ObligationEvent, ObligationEventName, ContractEvent, ContractEventName
from app.classes.spec.contract_spec_parameter import ContractSpecParameter as Parm
from app.classes.spec.other_predicates import *

arg_values = {
     'renter_id': 'renter',
     'landlord_id': 'landlord',
     'property_address': '123 Main Street',
     'rent_amount': 1500,
     'currency': 'CAD',
     'late_fee_amount': 500,
     'deposit_amount': 1000
}

def get_contract_spec(arg_dict: Dict[str,str] = arg_values):
    parameters = [
        Parm('renter_id', 'String'),
        Parm('landlord_id', 'String'),
        Parm('property_address', 'String'),
        Parm('rent_amount', 'Number'),
        Parm('currency', 'Currency'),
        Parm('late_fee_amount', 'Number'),
        Parm('deposit_amount', 'Number')
    ]

    # Declarations
    renter = RoleDeclaration(arg_dict["renter_id"], 'Renter')
    landlord = RoleDeclaration(arg_dict["landlord_id"], 'Landlord')
    RENTER = renter.to_obj()
    LANDLORD = landlord.to_obj()

    the_property = AssetDeclaration('property', 'RentalProperty', [
        DeclarationProp('address', f'"{arg_dict["property_address"]}"','String')
    ])
    PROPERTY = the_property.to_obj()

    evt_pay_rent = EventDeclaration('evt_pay_rent', 'Pay', [
        DeclarationProp('amount', arg_dict["rent_amount"], 'Number'),
        DeclarationProp('currency', f'Currency({arg_dict["currency"]})', 'Currency'),
        DeclarationProp('from', RENTER, 'Role'),
        DeclarationProp('to', LANDLORD, 'Role'),
    ])

    evt_pay_late = EventDeclaration('evt_pay_late', 'Pay', [
        DeclarationProp('amount', arg_dict["late_fee_amount"], 'Number'),
        DeclarationProp('currency', f'Currency({arg_dict["currency"]})', 'Currency'),
        DeclarationProp('from', RENTER, 'Role'),
        DeclarationProp('to', LANDLORD, 'Role'),
    ])

    evt_pay_deposit = EventDeclaration('evt_pay_deposit', 'Pay', [
        DeclarationProp('amount', arg_dict["deposit_amount"], 'Number'),
        DeclarationProp('currency', f'Currency({arg_dict["currency"]})', 'Currency'),
        DeclarationProp('from', RENTER, 'Role'),
        DeclarationProp('to', LANDLORD, 'Role'),
    ])

    evt_return_deposit = EventDeclaration('evt_return_deposit', 'Pay', [
        DeclarationProp('amount', arg_dict["deposit_amount"], 'Number'),
        DeclarationProp('currency', f'Currency({arg_dict["currency"]})', 'Currency'),
        DeclarationProp('from', LANDLORD, 'Role'),
        DeclarationProp('to', RENTER, 'Role'),
    ])

    evt_occupy_property = EventDeclaration('evt_occupy_property', 'OccupyProperty', [
        DeclarationProp('agent', RENTER, 'Role'),
        DeclarationProp('property', PROPERTY, 'RentalProperty'),
    ])

    evt_abandon_property = EventDeclaration('evt_abandon_property', 'AbandonProperty', [
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
    EVT_PAY_RENT = evt_pay_rent.to_obj()
    EVT_PAY_LATE = evt_pay_late.to_obj()
    EVT_PAY_DEPOSIT = evt_pay_deposit.to_obj()
    EVT_RETURN_DEPOSIT = evt_return_deposit.to_obj()
    EVT_OCCUPY_PROPERTY = evt_occupy_property.to_obj()
    EVT_ABANDON_PROPERTY = evt_abandon_property.to_obj()
    EVT_KEEP_PET = evt_keep_pet.to_obj()
    EVT_ALLOW_PETS = evt_allow_pets.to_obj()
    
    declarations = {
        'renter': renter,
        'landlord': landlord,
        'property': the_property,
        'evt_pay_rent': evt_pay_rent,
        'evt_pay_late': evt_pay_late,
        'evt_pay_deposit': evt_pay_deposit,
        'evt_return_deposit': evt_return_deposit,
        'evt_occupy_property': evt_occupy_property,
        'evt_abandon_property': evt_abandon_property,
        'evt_keep_pet': evt_keep_pet,
        'evt_allow_pets': evt_allow_pets
    }


    # Contract Spec
    contract_spec = ContractSpec(
        'PropertyRental',
        parameters = parameters,
        declarations = declarations,
        obligations = {
            'ob_pay_rent': Obligation(
                'ob_pay_rent',
                None,
                RENTER,
                LANDLORD,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_PAY_RENT)
                )
            ),
            'ob_late_payment': Obligation(
                'ob_late_payment',
                None,
                RENTER,
                LANDLORD,
                PropMaker.make(
                    PredicateFunctionHappens(ObligationEvent(ObligationEventName.Violated, 'ob_pay_rent')) 
                ),
                PropMaker.make(PredicateFunctionHappens(EVT_PAY_LATE))
            ),
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
            'ob_return_deposit': Obligation(
                'ob_return_deposit',
                None,
                LANDLORD,
                RENTER,
                PropMaker.make(PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))),
                PropMaker.make(PredicateFunctionHappens(EVT_RETURN_DEPOSIT))
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
            'pow_suspend_ob_no_pets': Power(
                'pow_suspend_ob_no_pets',
                PropMaker.make(PredicateFunctionHappens(EVT_ALLOW_PETS)),
                LANDLORD,
                RENTER,
                PropMaker.make_default(),
                PFObligation(PFObligationName.Suspended, 'ob_no_pets')
            ),
            'pow_termination_abandon': Power(
                'pow_termination_abandon',
                None,
                LANDLORD,
                RENTER,
                PropMaker.make(PredicateFunctionHappens(EVT_ABANDON_PROPERTY)),
                PFContract(PFContractName.Terminated)
            ),
        }
    )

    return contract_spec
