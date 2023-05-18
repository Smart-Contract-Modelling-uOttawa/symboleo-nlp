from app.classes.spec.symboleo_contract import SymboleoContract, ContractSpec, DomainModel
from app.classes.spec.norm import Norm, Obligation, Power, SurvivingObligation
from app.classes.spec.prop_maker import PropMaker
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.sym_event import VariableEvent, ObligationEvent, ObligationEventName, ContractEvent, ContractEventName
from app.classes.spec.sym_point import PointVDE, PointAtomContractEvent
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.sym_situation import ObligationState, ObligationStateName
from app.classes.spec.contract_spec_parameter import ContractSpecParameter
from app.classes.spec.other_predicates import *
from app.classes.spec.proposition import PAnd, PComparison, PEquality, Proposition, PNegAtom, PAtomStringLiteral, PComparisonOp
from app.src.helpers.declarer import Declarer

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
    seller = Declarer.declare(dm, 'roles', 'Seller', 'seller') # Need to add the props
    buyer = Declarer.declare(dm, 'roles', 'Buyer', 'buyer') # Need to add the props
    goods = Declarer.declare(dm, 'assets', 'Meat', 'goods', [
        ('quantity', 'qnt'),
        ('quality', 'qlt')
    ])
    evt_delivered = Declarer.declare(dm, 'events', 'Delivered', 'evt_delivered', [
        ('item', 'goods'),
        ('deliveryAddress', 'delAdd'),
        ('delDueDate', 'Date.add(effDate, delDueDateDays, days)')
    ])
    evt_paid_late = Declarer.declare(dm, 'events', 'PaidLate', 'evt_paid_late', [
        ('amount', '(1 + interestRate / 100) * amt'),
        ('currency', 'curr'),
        ('from', 'buyer'),
        ('to', 'seller')
    ])
    evt_paid = Declarer.declare(dm, 'events', 'Paid', 'evt_paid', [
        ('amount', 'amt'),
        ('currency', 'curr'),
        ('from', 'buyer'),
        ('to', 'seller'),
        ('payDueDate', 'payDueDate')
    ])
    evt_disclosed = Declarer.declare(dm, 'events', 'Disclosed', 'evt_disclosed', [])

    # Declarations
    declarations = {
        'seller': seller,
        'buyer': buyer,
        'goods': goods,
        'evt_delivered': evt_delivered,
        'evt_paid_late': evt_paid_late,
        'evt_paid': evt_paid,
        'evt_disclosed': evt_disclosed
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
            'ob_delivery': Obligation(
                'ob_delivery',
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionWHappensBefore(
                        DELIVERED_EVENT,
                        PointVDE('evt_delivered.delDueDate')
                    )
                )
            ),
            'ob_payment': Obligation(
                'ob_payment',
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionWHappensBefore(
                        PAID_EVENT,
                        PointVDE('evt_paid.payDueDate')
                    )
                )
            ),
            'ob_late_payment': Obligation(
                'ob_late_payment',
                PropMaker.make(
                    PredicateFunctionHappens(
                        ObligationEvent(ObligationEventName.Violated, 'ob_payment')
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

        # TODO: I think this should be a HappensWithin
        # HappensWithin(Terminated, Interval(START, Date.add(6, months, terminated)))
        surviving_obligations = {
            'so1': SurvivingObligation(
                'so1',
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionWHappensBefore(
                        DISCLOSED_EVENT, 
                        PointFunction(
                            PointAtomContractEvent(ContractEvent(ContractEventName.Terminated)),
                            6, 
                            TimeUnit.Months
                        )
                    ),
                    negation = True
                )
            ),
            'so2': SurvivingObligation(
                'so2',
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionWHappensBefore(
                        DISCLOSED_EVENT, 
                        PointFunction(
                            PointAtomContractEvent(ContractEvent(ContractEventName.Terminated)),
                            6, 
                            TimeUnit.Months
                        )
                    ),
                    negation = True
                )
            ) 
        },
        powers = {
            'pow_suspend_delivery': Power(
                'pow_suspend_delivery',
                PropMaker.make(
                    PredicateFunctionHappens(
                        ObligationEvent(ObligationEventName.Violated, 'ob_payment')
                    )
                ),
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PFObligation(PFObligationName.Suspended, 'ob_delivery')
            ),
            'pow_resume_ob_delivery': Power(
                'pow_resume_ob_delivery',
                PropMaker.make(
                    PredicateFunctionHappens(
                        ObligationEvent(ObligationEventName.Fulfilled, 'ob_late_payment')
                    )
                    # PredicateFunctionHappensWithin(
                    #     PAID_LATE_EVENT,
                    #     ObligationState(ObligationStateName.Suspension, 'ob_delivery')
                    # )
                ),
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PFObligation(PFObligationName.Resumed, 'ob_delivery')
            ),
            'pow_terminate_contract': Power(
                'pow_terminate_contract',
                PropMaker.make(
                    PredicateFunctionHappens(
                        ObligationEvent(ObligationEventName.Violated, 'ob_delivery')
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
