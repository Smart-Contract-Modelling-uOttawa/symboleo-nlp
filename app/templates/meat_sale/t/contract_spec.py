from typing import Dict, List
from app.classes.spec.symboleo_contract import SymboleoContract, ContractSpec, DomainModel
from app.classes.spec.norm import Norm, Obligation, Power, SurvivingObligation
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.declaration import RoleDeclaration, AssetDeclaration, EventDeclaration, DeclarationProp
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.sym_event import VariableEvent, ObligationEvent, ObligationEventName
from app.classes.spec.contract_spec_parameter import ContractSpecParameter as Parm
from app.classes.spec.other_predicates import *
from app.classes.spec.proposition import PAnd, PComparison, PEquality, Proposition, PNegAtom

arg_values = {
     'buyer_id': 'buyer',
     'seller_id': 'seller',
     'buyer_name': 'buyer',
     'seller_name': 'seller',
     'quantity_kg': '100',
     'quality': 'PRIME',
     'amount': '100',
     'currency': 'CAD',
     'interest_rate': '8',
    #  'delivery_due_date': 'March 18, 2024',
    #  'pay_due_date': 'March 30, 2024'
}

def get_contract_spec(arg_dict: Dict[str,str] = arg_values):
    parameters = [
        Parm('buyer_id', 'String'),
        Parm('seller_id', 'String'),
        Parm('buyer_name', 'String'),
        Parm('seller_name', 'String'),
        Parm('quantity_kg', 'Number'),
        Parm('quality', 'MeatQuality'),
        Parm('amount', 'Number'),
        Parm('currency', 'Currency'),
        Parm('interest_rate', 'Number'),
        # Parm('delivery_due_date', 'Date'),
        # Parm('pay_due_date', 'Date'),
    ]

    # Create the declarations
    seller = RoleDeclaration(arg_dict["seller_name"], 'Seller')
    buyer = RoleDeclaration(arg_dict["buyer_name"], 'Buyer')
    SELLER = seller.to_obj()
    BUYER = buyer.to_obj()

    goods = AssetDeclaration('goods', 'Meat', [
        DeclarationProp('quantity_kg', arg_dict["quantity_kg"], 'Number'),
        DeclarationProp('quality', f'MeatQuality({arg_dict["quality"]})', 'MeatQuality')
    ])
    GOODS = goods.to_obj()

    evt_deliver = EventDeclaration('evt_deliver', 'Deliver', [
        DeclarationProp('item', GOODS, 'Meat'),
        DeclarationProp('deliverer', SELLER, 'Role'),
        DeclarationProp('recipient', BUYER, 'Role')
    ])
    
    evt_pay = EventDeclaration('evt_pay', 'Pay', [
            DeclarationProp('amount', arg_dict["amount"], 'Number'),
            DeclarationProp('currency', f'Currency({arg_dict["currency"]})', 'Currency'),
            DeclarationProp('from', BUYER, 'Role'),
            DeclarationProp('to', SELLER, 'Role')
        ])

    evt_pay_interest = EventDeclaration('evt_pay_interest', 'PayInterest', [
            DeclarationProp('amount', f'"(1 + {arg_dict["interest_rate"]} / 100) * {arg_dict["amount"]}"', 'Number'),
            DeclarationProp('currency', f'Currency({arg_dict["currency"]})', 'Currency'),
            DeclarationProp('from', BUYER, 'Role'),
            DeclarationProp('to', SELLER, 'Role')
        ])
    
    evt_disclose = EventDeclaration('evt_disclose', 'Disclose')

    EVT_DELIVER = evt_deliver.to_obj()
    EVT_PAY = evt_pay.to_obj()
    EVT_PAY_INTEREST = evt_pay_interest.to_obj()
    EVT_DISCLOSE = evt_disclose.to_obj()

    # Declarations
    declarations = {
        'seller': seller,
        'buyer': buyer,
        'goods': goods,
        'evt_deliver': evt_deliver,
        'evt_pay_interest': evt_pay_interest,
        'evt_pay': evt_pay,
        'evt_disclose': evt_disclose
    }


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
                PropMaker.make(PredicateFunctionHappens(EVT_DELIVER))
            ),
            'ob_payment': Obligation(
                'ob_payment',
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(PredicateFunctionHappens(EVT_PAY))
            ),
            'ob_late_payment': Obligation(
                'ob_late_payment',
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_PAY_INTEREST)
                )
            )
        },


        surviving_obligations = {
            'so_disclosure_seller': SurvivingObligation(
                'so_disclosure_seller',
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(PredicateFunctionHappens(EVT_DISCLOSE), negation = True)
            ),
            'so_disclosure_buyer': SurvivingObligation(
                'so_disclosure_buyer',
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(PredicateFunctionHappens(EVT_DISCLOSE), negation = True)
            ) 
        },

        powers = {
            'pow_suspend_delivery': Power(
                'pow_suspend_delivery',
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PFObligation(PFObligationName.Suspended, 'ob_delivery')
            ),
            # 'pow_resume_ob_delivery': Power(
            #     'pow_resume_ob_delivery',
            #     PropMaker.make_default(False),
            #     BUYER,
            #     SELLER,
            #     PropMaker.make_default(),
            #     PFObligation(PFObligationName.Resumed, 'ob_delivery')
            # ),
            'pow_terminate_contract': Power(
                'pow_terminate_contract',
                PropMaker.make_default(False),
                BUYER,
                SELLER,
                PropMaker.make(
                    PredicateFunctionHappens(
                        ObligationEvent(ObligationEventName.Violated, 'ob_delivery')
                    ),
                    negation=True
                ),
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
            # Proposition([PAnd([PEquality(PComparison(
            #     PAtomStringLiteral('delivered.delDueDate'),
            #     PAtomStringLiteral('paid.payDueDate'),
            #     PComparisonOp.LT
            # ))])])
        ]
    )

    return contract_spec
