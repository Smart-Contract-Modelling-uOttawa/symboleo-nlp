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
from app.classes.spec.contract_spec_other import ContractSpecParameter
from app.src.helpers.declarer import Declarer
from app.classes.spec.other_function import *
from app.classes.spec.proposition import PAnd, PComparison, PEquality, Proposition, PNegAtom, PAtomStringLiteral, PComparisonOp

from app.templates.rental_agreement.t_raw.rental_domain import get_domain_model


def get_contract_spec():
    dm = get_domain_model()

    LANDLORD = 'landlord'
    RENTER = 'renter'

    parameters = [
        ContractSpecParameter('landlord', 'Landlord'),
        ContractSpecParameter('renter', 'Renter'),
        ContractSpecParameter('the_address', 'String'),
        ContractSpecParameter('the_currency', 'Currency'),
        ContractSpecParameter('the_rent_amount', 'Number'),
        ContractSpecParameter('the_payment_method', 'PaymentMethod'),
        ContractSpecParameter('the_late_fine', 'Number'),
        ContractSpecParameter('the_deposit_amount', 'Number'),
        ContractSpecParameter('days_in_advance', 'Number'),
        ContractSpecParameter('X', 'Date'),
    ]

    # Declarations
    the_property = Declarer.declare(dm, 'assets', 'RentalProperty', 'property', [
        ('address', 'the_address')
    ])
    evt_date_passes = Declarer.declare(dm, 'events', 'DatePasses', 'datePasses', [
        ('date', 'X')
    ])
    evt_pay_rent = Declarer.declare(dm, 'events', 'Paid', 'evt_pay_rent', [
        ('amount', 'the_rent_amount'),
        ('currency', 'the_currency'),
        ('paymentMethod', 'the_payment_method'),
        ('from', 'renter'),
        ('to', 'landlord')
    ])
    evt_pay_late_fine = Declarer.declare(dm, 'events', 'Paid', 'evt_pay_late_fine', [
        ('amount', 'the_late_fine'),
        ('currency', 'the_currency'),
        ('paymentMethod', 'the_payment_method'),
        ('from', 'renter'),
        ('to', 'landlord')
    ])
    evt_pay_deposit = Declarer.declare(dm, 'events', 'Paid', 'evt_pay_deposit', [
        ('amount', 'the_deposit_amount'),
        ('currency', 'the_currency'),
        ('paymentMethod', 'the_payment_method'),
        ('from', 'renter'),
        ('to', 'landlord')
    ])
    evt_return_deposit = Declarer.declare(dm, 'events', 'Paid', 'evt_return_deposit', [
        ('amount', 'the_deposit_amount'),
        ('currency', 'the_currency'),
        ('paymentMethod', 'the_payment_method'),
        ('from', 'landlord'),
        ('to', 'renter')
    ])
    evt_take_occupancy = Declarer.declare(dm, 'events', 'TakeOccupancy', 'evt_take_occupancy', [
        ('agent', 'renter')
    ])
    evt_renter_breach = Declarer.declare(dm, 'events', 'BreachAgreement', 'evt_renter_breach', [
        ('agent', 'renter')
    ])
    evt_landlord_breach = Declarer.declare(dm, 'events', 'BreachAgreement', 'evt_landlord_breach', [
        ('agent', 'landlord')
    ])
    evt_provides_written_notice = Declarer.declare(dm, 'events', 'ProvideWrittenNotice', 'evt_provides_written_notice', [
        ('agent', 'landlord'),
        ('daysInAdvance', 'days_in_advance'),
    ])
    evt_abandons = Declarer.declare(dm, 'events', 'Abandons', 'evt_abandons', [
        ('agent', 'renter'),
        ('property', 'the_property'),
    ])
    evt_enters = Declarer.declare(dm, 'events', 'Enters', 'evt_enters', [
        ('agent', 'landlord'),
        ('property', 'the_property'),
    ])
    evt_keep_pets = Declarer.declare(dm, 'events', 'KeepPets', 'evt_keep_pets', [
        ('agent', 'renter')
    ])
    evt_provide_pet_permission = Declarer.declare(dm, 'events', 'ProvidePetPermission', 'evt_provide_pet_permission', [
        ('grantor', 'landlord')
    ])


    # Declarations -  figure this out...
    declarations = {
        'evt_date_passes': evt_date_passes,
        'evt_pay_rent': evt_pay_rent,
        'evt_pay_late_fine': evt_pay_late_fine,
        'evt_pay_deposit': evt_pay_deposit,
        'evt_return_deposit': evt_return_deposit,
        'evt_take_occupancy': evt_take_occupancy,
        'evt_renter_breach': evt_renter_breach,
        'evt_landlord_breach': evt_landlord_breach,
        'evt_provides_written_notice': evt_provides_written_notice,
        'evt_abandons': evt_abandons,
        'evt_enters': evt_enters,
        'evt_keep_pets': evt_keep_pets,
        'evt_provide_pet_permission': evt_provide_pet_permission,

    }

    # Variables to use
    DATE_PASSES = evt_date_passes.to_obj()
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
                PropMaker.make(
                    PredicateFunctionHappens(DATE_PASSES)
                ),
                RENTER,
                LANDLORD,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(PAY_RENT)
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
                    PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))
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
