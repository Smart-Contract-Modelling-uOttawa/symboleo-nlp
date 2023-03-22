import copy
from app.classes.symboleo_contract import ContractSpec
from app.classes.spec.contract_spec import Obligation, Power
from app.classes.spec.prop_maker import PropMaker
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.contract_spec_other import ContractSpecParameter
from app.classes.spec.other_function import *
from app.classes.spec.proposition import PAnd, PComparison, PEquality, Proposition, PNegAtom, PAtomStringLiteral, PComparisonOp
from app.classes.spec.sym_situation import ObligationState, ObligationStateName
from app.src.helpers.declarer import Declarer

from app.templates.sample.t.sample_domain import get_domain_model

def get_contract_spec():
    dm = get_domain_model()

    SELLER = 'seller'
    BUYER = 'buyer'

    parameters = [
        ContractSpecParameter('buyer', 'Buyer'),
        ContractSpecParameter('seller', 'Seller'),
        ContractSpecParameter('qnt', 'Number'),
        ContractSpecParameter('qlt', 'MeatQuality'),
        ContractSpecParameter('amt', 'Number'),
        ContractSpecParameter('curr', 'Currency'),
        ContractSpecParameter('payDueDate', 'Date'),
        ContractSpecParameter('delAdd', 'String'),
        ContractSpecParameter('effDate', 'Date'),
        ContractSpecParameter('delDueDateDays', 'Number'),
        ContractSpecParameter('interestRate', 'Number')
    ]

    # Creating the objects
    goods = Declarer.declare(dm, 'assets', 'Meat', 'goods', [
        ('quantity', 'qnt'),
        ('quality', 'qlt')
    ])
    evt_delivered = Declarer.declare(dm, 'events', 'Delivered', 'delivered', [
        ('item', 'goods'),
        ('deliveryAddress', 'delAdd'),
        ('delDueDate', 'Date.add(effDate, delDueDateDays, days)')
    ])
    evt_paid_late = Declarer.declare(dm, 'events', 'PaidLate', 'paidLate', [
        ('amount', '(1 + interestRate / 100) * amt'),
        ('currency', 'curr'),
        ('from', 'buyer'),
        ('to', 'seller')
    ])
    evt_paid = Declarer.declare(dm, 'events', 'Paid', 'paid', [
        ('amount', 'amt'),
        ('currency', 'curr'),
        ('from', 'buyer'),
        ('to', 'seller'),
        ('payDueDate', 'payDueDate')
    ])
    evt_disclosed = Declarer.declare(dm, 'events', 'Disclosed', 'disclosed', [])

    # Declarations
    declarations = {
        'goods': goods,
        'delivered': evt_delivered,
        'paidLate': evt_paid_late,
        'paid': evt_paid,
        'disclosed': evt_disclosed
    }

    # Variables to use
    GOODS = goods.to_obj()
    DELIVERED_EVENT = evt_delivered.to_obj()
    PAID_EVENT = evt_paid.to_obj()
    PAID_LATE_EVENT = evt_paid_late.to_obj()
    DISCLOSED_EVENT = evt_disclosed.to_obj()

    # Contract Spec
    contract_spec = ContractSpec(
        'MeatSale',
        parameters = parameters,
        declarations = declarations,
        preconditions = [
            Proposition([PAnd([PEquality(PComparison(PNegAtom(
                PredicateFunctionIsOwner(GOODS, 'seller')
            )))])])
        ],
        postconditions = [
            Proposition([PAnd([
                PEquality(PComparison(PNegAtom(PredicateFunctionIsOwner(GOODS, 'buyer')))),
                PEquality(PComparison(PNegAtom(PredicateFunctionIsOwner(GOODS, 'seller'), negation=True)))
            ])])
        ],
        obligations = {
            'delivery': Obligation(
                'delivery',
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(DELIVERED_EVENT)
                )
            ),
            'payment': Obligation(
                'payment',
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(PAID_EVENT)
                )
            ),
            'latePayment': Obligation(
                'latePayment',
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(PAID_LATE_EVENT)
                )
            )
        },

        surviving_obligations = {
            'so1': Obligation(
                'so1',
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(DISCLOSED_EVENT),
                    negation = True
                )
            ),
            'so2': Obligation(
                'so2',
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(DISCLOSED_EVENT),
                    negation = True
                )
            ) 
        },
        powers = {
            'suspendDelivery': Power(
                'suspendDelivery',
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PFObligation(PFObligationName.Suspended, 'delivery')
            ),
            'resumeDelivery': Power(
                'resumeDelivery',
                PropMaker.make(
                    PredicateFunctionHappensWithin(
                        PAID_LATE_EVENT,
                        ObligationState(ObligationStateName.Suspension, 'delivery')
                    )
                ),
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PFObligation(PFObligationName.Resumed, 'delivery')
            ),
            'terminateContract': Power(
                'terminateContract',
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PFContract(PFContractName.Terminated)
            )
        },
        constraints = [
            Proposition([PAnd([PEquality(PComparison(PNegAtom(
                PredicateFunctionIsEqual('buyer', 'seller'), 
                negation=True
            )))])]),
            PropMaker.make_not_assigned('suspendDelivery'),
            PropMaker.make_not_assigned('resumeDelivery'),
            PropMaker.make_not_assigned('terminateContract'),
            PropMaker.make_not_assigned('delivery'),
            PropMaker.make_not_assigned('payment'),
            PropMaker.make_not_assigned('latePayment'),
            Proposition([PAnd([PEquality(PComparison(
                PAtomStringLiteral('delivered.delDueDate'),
                PAtomStringLiteral('paid.payDueDate'),
                PComparisonOp.LT
            ))])])
        ]
    )

    return contract_spec
