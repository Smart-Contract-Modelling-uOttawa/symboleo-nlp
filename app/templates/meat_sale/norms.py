from app.classes.spec.helpers import TimeValueInt, VariableDotExpression
from app.classes.spec.symboleo_spec import Obligation, PAnd, PEquality, PComparison, Power, Proposition
from app.classes.spec.p_atoms import PAtomPredicate, NegatedPAtom
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensWithin, PredicateFunctionWHappensBefore, PredicateFunctionOccurs
from app.classes.spec.sym_event import ContractEvent, VariableEvent, ObligationEvent
from app.classes.spec.interval import Interval, SituationExpression
from app.classes.spec.situation import ObligationState
from app.classes.spec.point import Point, PointAtomContractEvent, PointAtomParameterDotExpression, PointFunction
from app.classes.spec.power_function import PFObligation, PFContract

SELLER = VariableDotExpression('seller')
BUYER = VariableDotExpression('buyer')

PAID_EVENT = VariableEvent(
    VariableDotExpression('paid')
)

PAID_LATE_EVENT = VariableEvent(
    VariableDotExpression('paidLate')
)

DELIVERED_EVENT = VariableEvent(
    VariableDotExpression('delivered')
)

DISCLOSED_EVENT = VariableEvent(
    VariableDotExpression('disclosed')
)


## https://github.com/Smart-Contract-Modelling-uOttawa/Symboleo-IDE/blob/master/samples/MeatSaleContract.symboleo
meat_sale_norms = {
    'obligations': [
        ## delivery: O(seller, buyer, true, WhappensBefore(delivered, delivered.delDueDate))
        Obligation(
            'delivery',
            None,
            SELLER,
            BUYER,
            None,
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            PAtomPredicate(
                                PredicateFunctionWHappensBefore(
                                    DELIVERED_EVENT,
                                    Point(
                                        PointAtomParameterDotExpression(
                                            VariableDotExpression('delivered.delDueDate')
                                        )
                                    )
                                )
                            )
                        ])
                    ])
                ])
            ])
        ),

        ## payment: O(buyer, seller, true, WhappensBefore(paid, paid.payDueDate))
        Obligation(
            'payment',
            None,
            BUYER,
            SELLER,
            None,
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            PAtomPredicate(
                                PredicateFunctionWHappensBefore(
                                    PAID_EVENT,
                                    Point(
                                        PointAtomParameterDotExpression(
                                            VariableDotExpression('paid.payDueDate')
                                        )
                                    )
                                )
                            )
                        ])
                    ])
                ])
            ])
        ),

        ## latePayment: Happens(Violated(obligations.payment)) -> O(buyer, seller, true, Happens(paidLate))
        Obligation(
            'latePayment',
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            PAtomPredicate(
                                PredicateFunctionHappens(
                                    ObligationEvent('Violated', 'payment')
                                )
                            )
                        ])
                    ])
                ])
            ]),
            BUYER,
            SELLER,
            None,
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            PAtomPredicate(
                                PredicateFunctionHappens(
                                    PAID_LATE_EVENT
                                )
                            )
                        ])
                    ])
                ])
            ])
        )
    ],

    'surviving_obligations':[
        ## so1: O(seller, buyer, true, not WhappensBefore(disclosed, Date.add(Activated(self), 6, months)))
        Obligation(
            'so1',
            None,
            SELLER,
            BUYER,
            None,
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            NegatedPAtom(
                                PredicateFunctionWHappensBefore(
                                    DISCLOSED_EVENT,
                                    Point(
                                        PointFunction(
                                            PointAtomContractEvent(
                                                ContractEvent('Activated')
                                            ),
                                            TimeValueInt(6),
                                            'months'
                                        )
                                    )
                                )
                            )
                        ])
                    ])
                ])
            ])
        ),
        
        ## so2: O(buyer, seller, true, not WhappensBefore(disclosed, Date.add(Activated(self), 6, months)))
        Obligation(
            'so2',
            None,
            BUYER,
            SELLER,
            None,
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            NegatedPAtom(
                                PredicateFunctionWHappensBefore(
                                    DISCLOSED_EVENT,
                                    Point(
                                        PointFunction(
                                            PointAtomContractEvent(
                                                ContractEvent('Activated')
                                            ),
                                            TimeValueInt(6),
                                            'months'
                                        )
                                    )
                                )
                            )
                        ])
                    ])
                ])
            ])
        )
    ],

    'powers': [
        ## suspendDelivery : Happens(Violated(obligations.payment)) -> P(seller, buyer, true, Suspended(obligations.delivery))
        Power(
            'suspendDelivery',
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            PredicateFunctionHappens(
                                ObligationEvent('Violated', 'payment')
                            )
                        ])
                    ])
                ])
            ]),
            SELLER,
            BUYER,
            None,
            PFObligation('Suspended', 'delivery')
        ),

        ## resumeDelivery: HappensWithin(paidLate, Suspension(obligations.delivery)) -> P(buyer, seller, true, Resumed(obligations.delivery))
        Power(
            'resumeDelivery',
            Proposition([PAnd([PEquality([PComparison([
                PredicateFunctionHappensWithin(
                    PAID_LATE_EVENT,
                    Interval(
                        SituationExpression(
                            ObligationState('Suspension', 'delivery')
                        )
                    )
                )
            ])])])]),
            BUYER,
            SELLER,
            None,
            PFObligation('Resumed', 'delivery')
        ),
        
        ## terminateContract: Happens(Violated(obligations.delivery)) -> P(buyer, seller, true, Terminated(self))
        Power(
            'terminateContract',
            Proposition([PAnd([PEquality([PComparison([
                PredicateFunctionHappens(
                    ObligationEvent('Violated', 'delivery')
                )
            ])])])]),
            BUYER,
            SELLER,
            None,
            PFContract('Terminated')
        )
    ]
}