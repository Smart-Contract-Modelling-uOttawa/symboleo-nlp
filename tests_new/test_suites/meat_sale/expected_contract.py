from app.classes.spec.helpers import TimeValueInt, TimeUnitStr, VariableDotExpression
from app.classes.spec.symboleo_spec import Obligation, PAnd, PEquality, PComparison, Power, Proposition, PNegAtom
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensWithin, PredicateFunctionWHappensBefore, PredicateFunctionOccurs
from app.classes.spec.sym_event import ContractEvent, VariableEvent, ObligationEvent
from app.classes.spec.sym_interval import Interval, SituationExpression, Never, IntervalFunction, IntervalFunctionEnding
from app.classes.spec.sym_situation import ObligationState
from app.classes.spec.sym_point import Point, PointVDE, PointAtomContractEvent, PointAtomParameterDotExpression, PointFunction
from app.classes.spec.power_function import PFObligation, PFContract
from app.classes.symboleo_contract import SymboleoContract
from app.classes.symboleo_contract import DomainModel
from app.classes.domain_model.domain_model import Role, Asset, DomainEvent, DomainProp
from app.classes.symboleo_contract import ContractSpec


dm = DomainModel(
    roles = {
        'seller': Role('seller', [
            DomainProp('address', '123 Main street', 'str')
        ]),
        'buyer': Role('buyer', [
            DomainProp('address', '999 Central Ave', 'str')
        ])
    },
    events = {
        'delivered': DomainEvent('delivered', [
            DomainProp('item', 'meat', 'meat'),
            DomainProp('location', 'buyer.address', 'str')
        ]),

        'paid': DomainEvent('paid', [
            DomainProp('from', 'buyer', 'Role'), 
            DomainProp('to', 'seller', 'Role'),
            DomainProp('amount', '100', 'number'),
            DomainProp('currency', 'CAD', 'Currency'),
        ]),

        'paidLate': DomainEvent('paidLate', [
            DomainProp('from', 'buyer', 'Role'),
            DomainProp('to', 'seller', 'Role'),
            DomainProp('amount', '10% * paid.amount', 'number'),
            DomainProp('currency', 'paid.currency', 'Currency'),
        ]),

        'disclosed': DomainEvent('disclosed', [
        ])
        
    },
    assets = {
        'perishableGood': Asset('perishableGood', None, [
            DomainProp('quantity', '', 'number'),
            DomainProp('quality', '', 'MeatQuality')
        ]),
        'meat': Asset('meat', 'perishableGood')
    }
)

SELLER = dm.roles['seller'].to_obj()
BUYER = dm.roles['buyer'].to_obj()

DELIVERED_EVENT = dm.events['delivered'].to_obj()
PAID_EVENT = dm.events['paid'].to_obj()
PAID_LATE_EVENT = dm.events['paidLate'].to_obj()
DISCLOSED_EVENT = dm.events['disclosed'].to_obj()

contract_spec = ContractSpec(
    obligations = {
        # delivery: O(seller, buyer, true, WhappensBefore(delivered, Date.add(activated(self), 2, weeks)))
        'delivery': Obligation(
            'delivery',
            None,
            SELLER,
            BUYER,
            None,
            Proposition([PAnd([PEquality([PComparison([PAtomPredicate(
                PredicateFunctionWHappensBefore(
                    DELIVERED_EVENT,
                    PointFunction(
                        PointAtomContractEvent(ContractEvent('activated')),
                        TimeValueInt(2),
                        TimeUnitStr('weeks')
                    )
                )
            )])])])])
        ),

        # payment: O(buyer, seller, true, WhappensBefore(paid, April 17, 2022))
        'payment': Obligation(
            'payment',
            None,
            BUYER,
            SELLER,
            None,
            Proposition([PAnd([PEquality([PComparison([PAtomPredicate(
                PredicateFunctionWHappensBefore(
                    PAID_EVENT,
                    PointAtomParameterDotExpression(PointVDE('April 17, 2022'))
                )
            )])])])])
        ),

        # latePayment: Happens(Violated(obligations.payment)) -> O(buyer, seller, true, Happens(paidLate))
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

        ## disclosure1: O(seller, buyer, true, WhappensBefore(disclosed, Date.add(activated(self), 6, months)))
        'disclosure1': Obligation(
            'disclosure1',
            None,
            SELLER,
            BUYER,
            None,
            Proposition([PAnd([PEquality([PComparison([PNegAtom(PAtomPredicate(
                PredicateFunctionWHappensBefore(
                    DISCLOSED_EVENT,
                    PointFunction(
                        PointAtomContractEvent(ContractEvent('activated')),
                        TimeValueInt(6),
                        TimeUnitStr('months')
                    )
                )),True
            )])])])])
        ),

        ## disclosure2: O(buyer, seller, true, not Happens(disclosed))
        'disclosure2': Obligation(
            'disclosure2',
            None,
            BUYER,
            SELLER,
            None,
            Proposition([PAnd([PEquality([PComparison([PNegAtom(PAtomPredicate(
                PredicateFunctionWHappensBefore(
                    DISCLOSED_EVENT,
                    PointFunction(
                        PointAtomContractEvent(ContractEvent('activated')),
                        TimeValueInt(6),
                        TimeUnitStr('months')
                    )
                )),True
            )])])])])
        )

    },

    powers = {
        # suspendDelivery : Happens(Violated(obligations.payment)) -> P(seller, buyer, true, Suspended(obligations.delivery))
        'suspendDelivery': Power(
            'suspendDelivery',
            Proposition([PAnd([PEquality([PComparison([PNegAtom(
                PAtomPredicate(
                    PredicateFunctionHappens(
                        ObligationEvent('Violated', 'payment')
                    )
                )
            )])])])]),
            SELLER,
            BUYER,
            None,
            PFObligation('Suspended', 'delivery')
        ),

        # resumeDelivery: HappensWithin(paidLate, Suspension(obligations.delivery)) -> P(buyer, seller, true, Resumed(obligations.delivery))
        'resumeDelivery': Power(
            'resumeDelivery',
            Proposition([PAnd([PEquality([PComparison([PNegAtom(
                PAtomPredicate(
                    PredicateFunctionHappensWithin(
                        PAID_LATE_EVENT,
                        Interval(
                            SituationExpression(
                                ObligationState('Suspension', 'delivery')
                            )
                        )
                    )
                )
            )])])])]),
            BUYER,
            SELLER,
            None,
            PFObligation('Resumed', 'delivery')
        ),

        # terminateContract: Occurs(Violation(obligations.delivery), Interval(Date.add(delivery.delDueDate, 10, days), MAX_DATE) -> P(buyer, seller, true, Terminated(self))
        'terminateContract': Power(
            'terminateContract',
            Proposition(
                [
                    PAnd([PEquality([PComparison([PNegAtom(
                        PAtomPredicate(
                            PredicateFunctionOccurs(
                                ObligationState('Violation', 'delivery'),
                                Interval(
                                    IntervalFunctionEnding(
                                        PointFunction(
                                            PointAtomParameterDotExpression(PointVDE('delivery.delDueDate')),
                                            TimeValueInt(10),
                                            TimeUnitStr('days')
                                        )
                                    )
                                ) 
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


expected_contract = SymboleoContract(dm, contract_spec, None)
