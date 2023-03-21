import copy
from app.classes.symboleo_contract import SymboleoContract, ContractSpec, DomainModel
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

from app.src.helpers.template_helpers import TemplateHelpers as TH
from app.templates.sample.t_raw.sample_domain import get_domain_model

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
    goods = TH.create_declaration(dm, 'assets', 'Meat', 'goods', [
        ('quantity', 'qnt'),
        ('quality', 'qlt')
    ])
    evt_delivered = TH.create_declaration(dm, 'events', 'Delivered', 'delivered', [
        ('item', 'goods'),
        ('deliveryAddress', 'delAdd'),
        ('delDueDate', 'Date.add(effDate, delDueDateDays, days)')
    ])
    evt_paid_late = TH.create_declaration(dm, 'events', 'PaidLate', 'paidLate', [
        ('amount', '(1 + interestRate / 100) * amt'),
        ('currency', 'curr'),
        ('from', 'buyer'),
        ('to', 'seller')
    ])
    evt_paid = TH.create_declaration(dm, 'events', 'Paid', 'paid', [
        ('amount', 'amt'),
        ('currency', 'curr'),
        ('from', 'buyer'),
        ('to', 'seller'),
        ('payDueDate', 'payDueDate')
    ])
    evt_disclosed = TH.create_declaration(dm, 'events', 'Disclosed', 'disclosed', [])


    # Declarations
    declarations = {
        'goods': goods.to_declaration('Meat'),
        'delivered': evt_delivered.to_declaration('Delivered'),
        'paidLate': evt_paid_late.to_declaration('PaidLate'),
        'paid': evt_paid.to_declaration('Paid'),
        'disclosed': evt_disclosed.to_declaration('Disclosed')
    }

    # Variables to use
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
                PredicateFunctionIsOwner('goods', 'seller')
            )))])])
        ],
        postconditions = [
            Proposition([PAnd([
                PEquality(PComparison(PNegAtom(PredicateFunctionIsOwner('goods', 'buyer')))),
                PEquality(PComparison(PNegAtom(PredicateFunctionIsOwner('goods', 'seller'), negation=True)))
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
                    PredicateFunctionWHappensBefore(
                        DELIVERED_EVENT,
                        PointVDE('delivered.delDueDate') # Should I fix this reference?
                    )
                )
            ),
            'payment': Obligation(
                'payment',
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionWHappensBefore(
                        PAID_EVENT,
                        PointVDE('paid.payDueDate') # Should I fix this reference?
                    )
                )
            ),
            'latePayment': Obligation(
                'latePayment',
                PropMaker.make(
                    PredicateFunctionHappens(
                        ObligationEvent(ObligationEventName.Violated, 'payment')
                    )
                ),
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
                    PredicateFunctionWHappensBefore(
                        DISCLOSED_EVENT, 
                        PointFunction(
                            PointAtomContractEvent(ContractEvent(ContractEventName.Activated)),
                            6, 
                            TimeUnit.Months
                        )
                    ),
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
                    PredicateFunctionWHappensBefore(
                        DISCLOSED_EVENT, 
                        PointFunction(
                            PointAtomContractEvent(ContractEvent(ContractEventName.Activated)),
                            6, 
                            TimeUnit.Months
                        )
                    ),
                    negation = True
                )
            ) 
        },
        powers = {
            'suspendDelivery': Power(
                'suspendDelivery',
                PropMaker.make(
                    PredicateFunctionHappens(
                        ObligationEvent(ObligationEventName.Violated, 'payment')
                    )
                ),
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
                PropMaker.make(
                    PredicateFunctionHappens(
                        ObligationEvent(ObligationEventName.Violated, 'delivery')
                    )
                ),
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
