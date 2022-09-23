from app.classes.spec.atoms import EventProposition, SituationProposition, WithinAtom
from app.classes.spec.helpers import Interval, Point, Situation, SymEvent

from app.classes.spec.symboleo_spec import Junction, NegAtom, Power, Obligation, Proposition, Role


SELLER = Role('Seller')
BUYER = Role('Buyer')

meat_sale_norms = {
    'obligations': [
       Obligation(
        'O1',
        None,
        SELLER,
        BUYER,
        None,
        Proposition([
            Junction([
                NegAtom(
                    EventProposition(
                        SymEvent('delivered'),
                        Point('BEFORE delivered.delDueD')
                    )
                )
            ])
        ])
       ),

       Obligation(
        'O2',
        None,
        BUYER,
        SELLER,
        None,
        Proposition([
            Junction([
                NegAtom(
                    EventProposition(
                        SymEvent('paid'),
                        Point('PayDueD')
                    )
                )
            ])
        ])
       ),

       Obligation(
        'O3',
        Proposition([
            Junction([
                NegAtom(
                    SituationProposition(
                        Situation('oVIOLATION(O2)'),
                        Interval('X')
                    )
                )
            ])
        ]),
        BUYER,
        SELLER,
        None,
        Proposition([
            Junction([
                NegAtom(
                    EventProposition(
                        SymEvent('PaidLate'),
                        Point('X')
                    )
                )
            ])
        ])
       )
    ],

    'surviving_obligations':[
        Obligation(
            'SO1',
            None,
            SELLER,
            BUYER,
            None,
            Proposition([
                Junction([
                    NegAtom(
                        EventProposition(
                            SymEvent('disclosed'),
                            Point('t')
                        ),
                        negation=True
                    ),
                    NegAtom(
                        WithinAtom(
                            Point('t'),
                            Interval('6 Months after cActivated(meatSaleC)') ## Work to do here...
                        )
                    )
                ])
            ])
        ),

        Obligation(
            'SO2',
            None,
            BUYER,
            SELLER,
            None,
            Proposition([
                Junction([
                    NegAtom(
                        EventProposition(
                            SymEvent('disclosed'),
                            Point('t')
                        ),
                        True
                    ),
                    NegAtom(
                        WithinAtom(
                            Point('t'),
                            Interval('6 Months after cActivated(meatSaleC)') ## Work to do here...
                        )
                    )
                ])
            ])
        ),
    ],

    'powers': [
        Power(
            'P1',
            Proposition([
                Junction([
                    NegAtom(
                        SituationProposition(
                            Situation('oViolation(O2)'),
                            Interval('X')
                        )
                    )
                ])
            ]),
            SELLER,
            BUYER,
            None,
            Proposition([
                Junction([
                    NegAtom(
                        SituationProposition(
                            Situation('oSuspension(O1)'),
                            Interval('X')
                        )
                    )
                ])
            ])
        ),

        Power(
            'P2',
            Proposition([
                Junction([
                    NegAtom(
                        EventProposition(
                            SymEvent('PaidLate'),
                            Point('Within oSuspension(O1)')
                        )
                    )
                ])
            ]),
            BUYER,
            SELLER,
            None,
            Proposition([
                Junction([
                    NegAtom(
                        SituationProposition(
                            Situation('oInEffect(O1)'),
                            Interval('X')
                        )
                    )
                ])
            ])
        ),
        
        Power(
            'P3',
            Proposition([
                Junction([
                    NegAtom(
                        EventProposition(
                            SymEvent('Delivered'),
                            Point('10 days after DelDueDate')
                        ),
                        True
                    )
                ])
            ]),
            BUYER,
            SELLER,
            None,
            Proposition([
                Junction([
                    NegAtom(
                        SituationProposition(
                            Situation('oDischarge(O2)'),
                            Interval('X')
                        )
                    ),
                    NegAtom(
                        SituationProposition(
                            Situation('oDischarge(O3)'),
                            Interval('X')
                        )
                    ),
                    NegAtom(
                        SituationProposition(
                            Situation('cUnsuccessfTulermination(meatSaleC)'),
                            Interval('X')
                        )
                    )
                ])
            ])
        )
    ]
}