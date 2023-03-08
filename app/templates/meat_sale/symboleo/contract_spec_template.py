from app.classes.spec.contract_spec import Obligation, Power
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionOccurs, PredicateFunctionHappensWithin
from app.classes.spec.sym_event import ContractEvent, VariableEvent, ObligationEvent, ObligationEventName
from app.classes.spec.sym_interval import Interval, SituationExpression, Never, IntervalFunction
from app.classes.spec.sym_situation import ObligationState, ObligationStateName
from app.classes.spec.sym_point import Point, PointVDE, PointAtomContractEvent
from app.classes.spec.point_function import PointFunction
from app.classes.spec.power_function import PFObligation, PFContract, PFObligationName, PFContractName
from app.classes.spec.prop_maker import PropMaker

from app.classes.symboleo_contract import ContractSpec
from app.templates.meat_sale.symboleo.domain_model_template import meat_sale_domain_model_template as dm

SELLER = dm.roles['seller'].to_obj()
BUYER = dm.roles['buyer'].to_obj()

DELIVERED_EVENT = dm.events['delivered'].to_obj()
PAID_EVENT = dm.events['paid'].to_obj()
PAID_LATE_EVENT = dm.events['paidLate'].to_obj()
DISCLOSED_EVENT = dm.events['disclosed'].to_obj()

## https://github.com/Smart-Contract-Modelling-uOttawa/Symboleo-IDE/blob/master/samples/MeatSaleContract.symboleo
meat_sale_contract_spec_template = ContractSpec(
    'MeatSale',
    obligations = {
        # delivery: O(seller, buyer, true, Happens(delivered))
        'delivery': Obligation(
            'delivery',
            PropMaker.make_default(),
            SELLER,
            BUYER,
            PropMaker.make_default(),
            PropMaker.make(PredicateFunctionHappens(DELIVERED_EVENT))
        ),

        # payment: O(buyer, seller, true, Happens(paid))
        'payment': Obligation(
            'payment',
            PropMaker.make_default(),
            BUYER,
            SELLER,
            PropMaker.make_default(),
            PropMaker.make(PredicateFunctionHappens(PAID_EVENT)),
        ),

        #latePayment: Happens(Violated(obligations.payment)) -> O(buyer, seller, true, Happens(paidLate))
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
            PropMaker.make(PredicateFunctionHappens(PAID_LATE_EVENT))
        ),

        ## disclosure1: O(seller, buyer, true, not Happens(disclosed))
        'disclosure1': Obligation(
            'disclosure1',
            PropMaker.make_default(),
            SELLER,
            BUYER,
            PropMaker.make_default(),
            PropMaker.make(PredicateFunctionHappens(DISCLOSED_EVENT), True)
        ),

        ## disclosure2: O(buyer, seller, true, not Happens(disclosed))
        'disclosure2': Obligation(
            'disclosure2',
            PropMaker.make_default(),
            BUYER,
            SELLER,
            PropMaker.make_default(),
            PropMaker.make(PredicateFunctionHappens(DISCLOSED_EVENT), True)
        )
    },

    powers = {
        # suspendDelivery : P(seller, buyer, true, Suspended(obligations.delivery))
        'suspendDelivery': Power(
            'suspendDelivery',
            PropMaker.make_default(),
            #PropMaker.make(PredicateFunctionHappens(ObligationEvent(ObligationEventName.Violated, 'payment'))),
            SELLER,
            BUYER,
            PropMaker.make_default(),
            PFObligation(PFObligationName.Suspended, 'delivery')
        ),

        # TODO: Review this!
        ## resumeDelivery: Never -> P(buyer, seller, true, Resumed(obligations.delivery))
        ## resumeDelivery: HappensWithin(paidLate, Suspension(obligations.delivery)) -> P(buyer, seller, true, Resumed(obligations.delivery))
        'resumeDelivery': Power(
            'resumeDelivery',
            PropMaker.make_default(False),
            # PropMaker.make(
            #     PredicateFunctionHappensWithin(
            #         PAID_LATE_EVENT,
            #         Interval(SituationExpression(ObligationState(ObligationStateName.Suspension, 'delivery')))
            #     )
            # )
            BUYER,
            SELLER,
            PropMaker.make_default(),
            PFObligation(PFObligationName.Resumed, 'delivery')
        ),

        # TODO: Review this!
        ## terminateContract: Occurs(Violation(obligations.delivery)) -> P(buyer, seller, true, Terminated(self))
        'terminateContract': Power(
            'terminateContract',
            PropMaker.make(
                PredicateFunctionOccurs(
                    ObligationState(ObligationStateName.Violation, 'delivery'),
                    Never()
                )
            ),
            BUYER,
            SELLER,
            PropMaker.make_default(),
            PFContract(PFContractName.Terminated)
        )
    } 
)
