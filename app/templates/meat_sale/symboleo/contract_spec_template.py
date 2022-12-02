from app.classes.spec.helpers import TimeValueInt, TimeUnitStr, VariableDotExpression
from app.classes.spec.symboleo_spec import Obligation, PAnd, PEquality, PComparison, Power, Proposition, PNegAtom
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensWithin, PredicateFunctionWHappensBefore, PredicateFunctionOccurs
from app.classes.spec.sym_event import ContractEvent, VariableEvent, ObligationEvent
from app.classes.spec.sym_interval import Interval, SituationExpression, Never, IntervalFunction
from app.classes.spec.sym_situation import ObligationState
from app.classes.spec.sym_point import Point, PointVDE, PointAtomContractEvent, PointAtomParameterDotExpression, PointFunction
from app.classes.spec.power_function import PFObligation, PFContract

from app.classes.symboleo_contract import ContractSpec
from app.templates.meat_sale.symboleo.domain_model_template import meat_sale_domain_model_template as dm

SELLER = dm.roles['seller'].to_obj()
BUYER = dm.roles['buyer'].to_obj()

DELIVERED_EVENT = dm.events['delivered'].to_obj()
PAID_EVENT = dm.events['paid'].to_obj()
PAID_LATE_EVENT = dm.events['paidLate'].to_obj()
DISCLOSED_EVENT = dm.events['disclosed'].to_obj()

meat_sale_contract_spec_template = ContractSpec(
    obligations = {
        # delivery: O(seller, buyer, true, Happens(delivered))
        'delivery': Obligation(
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
                                PredicateFunctionHappens(
                                    DELIVERED_EVENT
                                )
                            )
                        ])
                    ])
                ])
            ])
        ),

        # payment: O(buyer, seller, true, Happens(paid))
        'payment': Obligation(
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
                                PredicateFunctionHappens(
                                    PAID_EVENT
                                )
                            )
                        ])
                    ])
                ])
            ])
        ),

        #latePayment: Happens(Violated(obligations.payment)) -> O(buyer, seller, true, Happens(paidLate))
        'latePayment': Obligation(
            'latePayment',
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            PNegAtom(
                                PAtomPredicate(
                                    PredicateFunctionHappens(
                                        ObligationEvent('Violated', 'payment')
                                    )
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
                            PNegAtom(
                                PAtomPredicate(
                                    PredicateFunctionHappens(
                                        PAID_LATE_EVENT
                                    )
                                )
                            )
                        ])
                    ])
                ])
            ])
        ),

        ## disclosure1: O(seller, buyer, true, not Happens(disclosed))
        'disclosure1': Obligation(
            'disclosure1',
            None,
            SELLER,
            BUYER,
            None,
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            PNegAtom(
                                PAtomPredicate(
                                    PredicateFunctionHappens(
                                        DISCLOSED_EVENT
                                    )
                                ),
                                True
                            )
                        ])
                    ])
                ])
            ])
        ),

        ## disclosure2: O(buyer, seller, true, not Happens(disclosed))
        'disclosure2': Obligation(
            'disclosure2',
            None,
            BUYER,
            SELLER,
            None,
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            PNegAtom(
                                PAtomPredicate(
                                    PredicateFunctionHappens(
                                        DISCLOSED_EVENT
                                    )
                                ),
                                True
                            )
                        ])
                    ])
                ])
            ])
        )

    },

    powers = {
        # suspendDelivery : P(seller, buyer, true, Suspended(obligations.delivery))
        'suspendDelivery': Power(
            'suspendDelivery',
            None,
            # Proposition([PAnd([PEquality([PComparison([PNegAtom(
            #     PAtomPredicate(
            #         PredicateFunctionHappens(
            #             ObligationEvent('Violated', 'payment')
            #         )
            #     )
            # )])])])]),
            SELLER,
            BUYER,
            None,
            PFObligation('Suspended', 'delivery')
        ),

        ## resumeDelivery: Never -> P(buyer, seller, true, Resumed(obligations.delivery))
        ## resumeDelivery: HappensWithin(paidLate, Suspension(obligations.delivery)) -> P(buyer, seller, true, Resumed(obligations.delivery))
        'resumeDelivery': Power(
            'resumeDelivery',
            None, # This should be a "never", e.g. Happens(False) or somethnig like that
            # Proposition([PAnd([PEquality([PComparison([PNegAtom(
            #     PAtomPredicate(
            #         PredicateFunctionHappensWithin(
            #             PAID_LATE_EVENT,
            #             Interval(
            #                 SituationExpression(
            #                     ObligationState('Suspension', 'delivery')
            #                 )
            #             )
            #         )
            #     )
            # )])])])]),
            BUYER,
            SELLER,
            None,
            PFObligation('Resumed', 'delivery')
        ),

        ## terminateContract: Happens(Violated(obligations.delivery)) -> P(buyer, seller, true, Terminated(self))
        'terminateContract': Power(
            'terminateContract',
            Proposition(
                [
                    PAnd([PEquality([PComparison([PNegAtom(
                        PAtomPredicate(
                            PredicateFunctionOccurs(
                                ObligationState('Violation', 'delivery'),
                                Never()
                                # Interval(
                                #     IntervalFunction(
                                #         PointAtomParameterDotExpression(PointVDE('delivery.delDueDate')),
                                #         PointFunction(
                                #             PointAtomParameterDotExpression(PointVDE('delivery.delDueDate')),
                                #             TimeValueInt(10),
                                #             TimeUnitStr('days')
                                #         )
                                #     )
                                # )
                                
                            )
                        )
                    )])])]),
                    
                ]
            ),
            BUYER,
            SELLER,
            None,
            PFContract('Terminated')
        )
    } 
)
