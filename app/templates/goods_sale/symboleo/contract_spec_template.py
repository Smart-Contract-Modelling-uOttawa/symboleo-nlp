from app.classes.spec.helpers import TimeValueInt, TimeUnitStr, VariableDotExpression
from app.classes.spec.proposition import PAnd, PEquality, PComparison, PNegAtom, Proposition
from app.classes.spec.contract_spec import Obligation, Power
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensWithin, PredicateFunctionWHappensBefore, PredicateFunctionOccurs
from app.classes.spec.sym_event import ObligationEvent
from app.classes.spec.power_function import PFContract

from app.classes.symboleo_contract import ContractSpec
from app.templates.goods_sale.symboleo.domain_model_template import goods_sale_domain_model_template as dm

SELLER = dm.roles['seller'].to_obj()
CUSTOMER = dm.roles['customer'].to_obj()

SELL_EVENT = dm.events['sellGoods'].to_obj()
DELIVER_EVENT = dm.events['deliverGoods'].to_obj()
PAY_EVENT = dm.events['payInvoice'].to_obj()
PAY_LATE_EVENT = dm.events['payLate'].to_obj()
PROVIDE_INVOICE_EVENT = dm.events['provideInvoice'].to_obj()
PROVIDE_TERMINATION_NOTICE_EVENT = dm.events['provideTerminationNotice'].to_obj() 

##TODO: Add the link
## https://github.com/Smart-Contract-Modelling-uOttawa/Symboleo-IDE/blob/master/samples/MeatSaleContract.symboleo
goods_sale_contract_spec_template = ContractSpec(
    obligations = {
        # sell: O(seller, customer, true, Happens(deliverGoods))
        'O_sellGoods': Obligation(
            'O_sellGoods',
            None,
            SELLER,
            CUSTOMER,
            None,
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            PAtomPredicate(
                                PredicateFunctionHappens(
                                    DELIVER_EVENT
                                )
                            )
                        ])
                    ])
                ])
            ])
        ),

        # invoice: O(seller, customer, true, Happens(provideInvoice))
        'O_provideInvoice': Obligation(
            'O_provideInvoice',
            None,
            SELLER,
            CUSTOMER,
            None,
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            PAtomPredicate(
                                PredicateFunctionHappens(
                                    PROVIDE_INVOICE_EVENT
                                )
                            )
                        ])
                    ])
                ])
            ])
        ),

        # payment: O(customer, seller, true, Happens(pay_invoice))
        'O_payInvoice': Obligation(
            'O_payInvoice',
            None,
            CUSTOMER,
            SELLER,
            None,
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            PAtomPredicate(
                                PredicateFunctionHappens(
                                    PAY_EVENT
                                )
                            )
                        ])
                    ])
                ])
            ])
        ),

        #payLate: Happens(Violated(obligations.payment)) -> O(buyer, seller, true, Happens(paidLate))
        'O_payLate': Obligation(
            'O_payLate',
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            PNegAtom(
                                PAtomPredicate(
                                    PredicateFunctionHappens(
                                        ObligationEvent('Violated', 'O_payInvoice')
                                    )
                                )
                            )
                        ])
                    ])
                ])
            ]),
            CUSTOMER,
            SELLER,
            None,
            Proposition([
                PAnd([
                    PEquality([
                        PComparison([
                            PNegAtom(
                                PAtomPredicate(
                                    PredicateFunctionHappens(
                                        PAY_LATE_EVENT
                                    )
                                )
                            )
                        ])
                    ])
                ])
            ])
        ),
    },

    powers = {
        ## terminateContract: Happens(provideTerminationNotice) -> P(customer, seller, true, Terminated(self))
        'O_terminateContract1': Power(
            'O_terminateContract1',
            Proposition(
                [
                    PAnd([PEquality([PComparison([PNegAtom(
                        PAtomPredicate(
                            PredicateFunctionHappens(
                                PROVIDE_TERMINATION_NOTICE_EVENT  
                            )
                        )
                    )])])]),
                    
                ]
            ),
            CUSTOMER,
            SELLER,
            None,
            PFContract('Terminated')
        ),

        ## terminateContract2: Happens(provideTerminationNotice) -> P(seller, customer, true, Terminated(self))
        'O_terminateContract2': Power(
            'O_terminateContract2',
            Proposition(
                [
                    PAnd([PEquality([PComparison([PNegAtom(
                        PAtomPredicate(
                            PredicateFunctionHappens(
                                PROVIDE_TERMINATION_NOTICE_EVENT  
                            )
                        )
                    )])])]),
                    
                ]
            ),
            CUSTOMER,
            SELLER,
            None,
            PFContract('Terminated')
        )
    } 
)
