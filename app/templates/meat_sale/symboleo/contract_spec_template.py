from app.classes.spec.helpers import TimeValueInt, TimeUnitStr, VariableDotExpression
from app.classes.spec.symboleo_spec import Obligation, PAnd, PEquality, PComparison, Power, Proposition, PNegAtom
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensWithin, PredicateFunctionWHappensBefore
from app.classes.spec.sym_event import ContractEvent, VariableEvent, ObligationEvent
from app.classes.spec.sym_interval import Interval, SituationExpression
from app.classes.spec.sym_situation import ObligationState
from app.classes.spec.sym_point import Point, PointAtomContractEvent, PointAtomParameterDotExpression, PointFunction
from app.classes.spec.power_function import PFObligation, PFContract

from app.classes.symboleo_contract import ContractSpec
from app.templates.meat_sale.symboleo.domain_model_template import meat_sale_domain_model_template as dm

SELLER = dm.roles['seller'].to_obj()
BUYER = dm.roles['buyer'].to_obj()

DELIVERED_EVENT = dm.events['delivered'].to_obj()
PAID_EVENT = dm.events['paid'].to_obj()
PAID_LATE_EVENT = dm.events['paidLate'].to_obj()

meat_sale_contract_spec_template = ContractSpec(
    obligations = {
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
        ) 

    },

    powers = {} #...
)

