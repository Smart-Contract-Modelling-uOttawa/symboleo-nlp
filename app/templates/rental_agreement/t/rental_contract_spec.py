from app.classes.symboleo_contract import ContractSpec
from app.classes.spec.domain_model import DomainObject
from app.classes.spec.contract_spec import Norm, Obligation, Power
from app.classes.spec.prop_maker import PropMaker
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.contract_spec_other import ContractSpecParameter
from app.src.helpers.declarer import Declarer
from app.classes.spec.other_function import *

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
        ContractSpecParameter('X', 'Date'),
    ]

    # Declarations
    the_property = Declarer.declare(dm, 'assets', 'RentalProperty', 'the_property', [
        ('address', 'the_address')
    ])
    evt_date_passes = Declarer.declare(dm, 'events', 'DatePasses', 'evt_date_passes', [
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
    evt_keep_pets = Declarer.declare(dm, 'events', 'KeepPets', 'evt_keep_pets', [
        ('agent', 'renter')
    ])

    declarations = {
        'the_property': the_property,
        'evt_date_passes': evt_date_passes,
        'evt_pay_rent': evt_pay_rent,
        'evt_pay_late_fine': evt_pay_late_fine,
        'evt_pay_deposit': evt_pay_deposit,
        'evt_return_deposit': evt_return_deposit,
        'evt_keep_pets': evt_keep_pets,
    }

    # Variables to use
    DATE_PASSES = evt_date_passes.to_obj()
    PAY_RENT = evt_pay_rent.to_obj()
    PAY_LATE_FINE = evt_pay_late_fine.to_obj()
    PAY_DEPOSIT = evt_pay_deposit.to_obj()
    RETURN_DEPOSIT = evt_return_deposit.to_obj()
    KEEP_PETS = evt_keep_pets.to_obj()

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
                None,
                RENTER,
                LANDLORD,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(PAY_LATE_FINE)
                )
            ),
            'pay_security_deposit': Obligation(
                'pay_security_deposit',
                None,
                RENTER,
                LANDLORD,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(PAY_DEPOSIT)
                )
            ),
            'return_deposit': Obligation(
                'return_deposit',
                None,
                LANDLORD,
                RENTER,
                PropMaker.make_default(), 
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
        },
        constraints = [
            ###...
        ]
    )

    return contract_spec
