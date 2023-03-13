import copy
from typing import List
from app.classes.symboleo_contract import SymboleoContract, ContractSpec, DomainModel
from app.classes.spec.domain_model import DomainObject
from app.classes.spec.contract_spec import Norm, Obligation, Power
from app.classes.spec.prop_maker import PropMaker
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.sym_event import VariableEvent, ObligationEvent, ObligationEventName, ContractEvent, ContractEventName
from app.classes.spec.sym_point import PointVDE, PointAtomContractEvent
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.sym_situation import ObligationState, ObligationStateName
from app.classes.spec.contract_spec_other import ContractSpecParameter, SymVariable, Assignment
from app.classes.spec.other_function import *
from app.classes.spec.proposition import PAnd, PComparison, PEquality, Proposition, PNegAtom, PAtomStringLiteral, PComparisonOp

from app.templates.sample.t_raw.sample_domain import get_domain_model

# Helper
def create_declaration(dm: DomainModel, obj_type: str, obj_name: str, obj_key: str, props:List = []):
    dm_obj: DomainObject = copy.deepcopy(dm.__dict__[obj_type][obj_name])
    dm_obj.name = obj_key
    for k,v in props:
        dm_obj.set_prop(k, v)
    return dm_obj

def get_contract_spec():
    dm = get_domain_model()

    LANDLORD = 'landlord'
    RENTER = 'renter'

    parameters = [
        ContractSpecParameter('landlord', 'Landlord'),
        ContractSpecParameter('renter', 'Renter'),
        ContractSpecParameter('_address', 'String'),
        ContractSpecParameter('_currency', 'Currency'),
        ContractSpecParameter('_rent_amount', 'Number'),
        ContractSpecParameter('_payment_method', 'PaymentMethod'),
        ContractSpecParameter('_late_fine', 'Number'),
        ContractSpecParameter('_deposit_amount', 'Number')
    ]

    # Creating the objects
    # TODO: May create a helper function for this...
    the_property = create_declaration(dm, 'assets', 'Property', 'property', [
        ('address', '_address')
    ])
    evt_pay_rent = create_declaration(dm, 'events', 'Paid', 'evt_pay_rent', [
        ('amount', '_rent_amount'),
        ('currency', '_currency'),
        ('method', '_payment_method'),
        ('from', 'renter'),
        ('to', 'landlord')
    ])
    evt_pay_late_fine = create_declaration(dm, 'events', 'Paid', 'evt_pay_late_fine', [
        ('amount', '_late_fine'),
        ('currency', '_currency'),
        ('method', '_payment_method'),
        ('from', 'renter'),
        ('to', 'landlord')
    ])
    evt_pay_deposit = create_declaration(dm, 'events', 'Paid', 'evt_pay_deposit', [
        ('amount', '_deposit_amount'),
        ('currency', '_currency'),
        ('method', '_payment_method'),
        ('from', 'renter'),
        ('to', 'landlord')
    ])
    evt_return_deposit = create_declaration(dm, 'events', 'Paid', 'evt_return_deposit', [
        ('amount', '_deposit_amount'),
        ('currency', '_currency'),
        ('method', '_payment_method'),
        ('from', 'landlord'),
        ('to', 'renter')
    ])
    evt_take_occupancy = create_declaration(dm, 'events', 'TakeOccupancy', 'evt_take_occupancy', [
        ('agent', 'renter')
    ])
    evt_renter_breach = create_declaration(dm, 'events', 'BreachAgreement', 'evt_renter_breach', [
        ('agent', 'renter')
    ])
    evt_landlord_breach = create_declaration(dm, 'events', 'BreachAgreement', 'evt_landlord_breach', [
        ('agent', 'landlord')
    ])
    evt_provides_written_notice = create_declaration(dm, 'events', 'ProvideWrittenNotice', 'evt_provides_written_notice', [
        ('agent', 'landlord'),
        ('daysInAdvance', '_daysInAdvance'),
    ])
    evt_abandons = create_declaration(dm, 'events', 'Abandons', 'evt_abandons', [
        ('agent', 'renter'),
        ('property', 'the_property'),
    ])
    evt_enters = create_declaration(dm, 'events', 'Enters', 'evt_enters', [
        ('agent', 'landlord'),
        ('property', 'the_property'),
    ])
    evt_keep_pets = create_declaration(dm, 'events', 'KeepPets', 'evt_keep_pets', [
        ('agent', 'renter')
    ])
    evt_provide_pet_permission = create_declaration(dm, 'events', 'ProvidePetPermission', 'evt_provide_pet_permission', [
        ('grantor', 'landlord')
    ])


    # Declarations
    declarations = {}
    # declarations = {
    #     'goods': goods.to_declaration('Meat'),
    #     'delivered': evt_delivered.to_declaration('Delivered'),
    #     'paidLate': evt_paid_late.to_declaration('PaidLate'),
    #     'paid': evt_paid.to_declaration('Paid'),
    #     'disclosed': evt_disclosed.to_declaration('Disclosed')
    # }

    # Variables to use
    PAY_RENT = evt_pay_rent.to_obj()
    PAY_LATE_FINE = evt_pay_late_fine.to_obj()
    PAY_DEPOSIT = evt_pay_deposit.to_obj()
    RETURN_DEPOSIT = evt_return_deposit.to_obj()
    TAKE_OCCUPANCY = evt_take_occupancy.to_obj()
    RENTER_BREACH = evt_renter_breach.to_obj()
    LANDLORD_BREACH = evt_landlord_breach.to_obj()
    PROVIDE_WRITTEN_NOTICE = evt_provides_written_notice.to_obj()
    ABANDONS = evt_abandons.to_obj()
    ENTERS = evt_enters.to_obj()
    KEEP_PETS = evt_keep_pets.to_obj()
    PROVIDE_PET_PERMISSION = evt_provide_pet_permission.to_obj()

    # Contract Spec
    contract_spec = ContractSpec(
        'PropertyRental',
        parameters = parameters,
        declarations = declarations,
        preconditions = [
            ###
        ],
        postconditions = [
            ###
        ],
        obligations = {
            'pay_rent': Obligation(
                'pay_rent',
                None,
                RENTER,
                LANDLORD,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(PAY_RENT) ## Make this have a frequency
                )
            ),
            'late_payment': Obligation(
                'late_payment',
                PropMaker.make(
                    PredicateFunctionHappens(ObligationEvent(ObligationEventName.Violated, 'pay_rent')) 
                ),
                RENTER,
                LANDLORD,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(
                        PAY_LATE_FINE
                    )
                )
            ),
            'pay_security_deposit': Obligation(
                'pay_security_deposit',
                None,
                RENTER,
                LANDLORD,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionWHappensBeforeEvent(PAY_DEPOSIT, TAKE_OCCUPANCY)
                )
            ),
            'return_deposit': Obligation(
                'return_deposit',
                PropMaker.make(
                    PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated) )
                ),
                LANDLORD,
                RENTER,
                PropMaker.make_default(), # Might add some more here...
                PropMaker.make(
                    PredicateFunctionHappens(RETURN_DEPOSIT)
                )
            ),
            'no_pets': Obligation(
                'no_pets',
                None,
                RENTER,
                LANDLORD,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(KEEP_PETS),
                    negation=True
                )
            ),
        },

        surviving_obligations = {
        },
        
        powers = {
            'terminate_breach1': Power(
                'terminate_breach1',
                PropMaker.make(
                    PredicateFunctionHappens(RENTER_BREACH)
                ),
                LANDLORD,
                RENTER,
                PropMaker.make_default(),
                PFContract(PFContractName.Terminated)
            ),
            'terminate_breach2': Power(
                'terminate_breach2',
                PropMaker.make(
                    PredicateFunctionHappens(LANDLORD_BREACH)
                ),
                RENTER,
                LANDLORD,
                PropMaker.make_default(),
                PFContract(PFContractName.Terminated)
            ),
            'terminate_notice': Power(
                'terminate_notice',
                PropMaker.make(
                    PredicateFunctionHappens(PROVIDE_WRITTEN_NOTICE)
                ),
                RENTER,
                LANDLORD,
                PropMaker.make_default(),
                PFContract(PFContractName.Terminated)
            ),
            'allow_pets': Power(
                'allow_pets',
                PropMaker.make(
                    PredicateFunctionHappens(PROVIDE_PET_PERMISSION)
                ),
                RENTER,
                LANDLORD,
                PropMaker.make_default(),
                PFObligation(PFObligationName.Suspended, 'no_pets')
            ),
            'terminate_abandon': Power(
                'terminate_abandon',
                PropMaker.make(
                    PredicateFunctionHappens(ABANDONS)
                ),
                LANDLORD,
                RENTER,
                PropMaker.make_default(),
                PFContract(PFContractName.Terminated)
            ),
        },
        constraints = [
            ###...
        ]
    )

    return contract_spec
