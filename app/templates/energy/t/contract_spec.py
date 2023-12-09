from typing import Dict, List
from app.classes.spec.symboleo_contract import SymboleoContract, ContractSpec, DomainModel
from app.classes.spec.norm import Norm, Obligation, Power, SurvivingObligation
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.declaration import RoleDeclaration, AssetDeclaration, EventDeclaration, DeclarationProp
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.sym_event import VariableEvent, ObligationEvent, ObligationEventName, ContractEvent, ContractEventName
from app.classes.spec.sym_point import PointVDE, PointAtomContractEvent
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.sym_situation import ObligationState, ObligationStateName
from app.classes.spec.contract_spec_parameter import ContractSpecParameter as Parm
from app.classes.spec.other_predicates import *
from app.classes.spec.proposition import PAnd, PComparison, PEquality, Proposition, PNegAtom, PAtomStringLiteral, PComparisonOp

arg_values = {
     'prosumer_id': 'prosumer',
     'buyer_id': 'buyer',
     'energy_qnt': '<energy_qnt>',
     'amount': '<amount>',
     'currency': 'CAD',
     'percentage': '<percentage>',
     'voltage': '<voltage>',
     'min_voltage': '<min>',
     'max_voltage': '<max>'
}

def get_contract_spec(arg_dict: Dict[str,str] = arg_values):
    parameters = [
        Parm('prosumer_id', 'String'),
        Parm('buyer_id', 'String'),
        Parm('amount_kw', 'Number'),
        Parm('amount', 'Number'),
        Parm('currency', 'Currency'),
        Parm('percentage', 'Number'),
        Parm('voltage', 'Number'),
        Parm('min_voltage', 'Number'),
        Parm('max_voltage', 'Number'), 
    ]

    # Create the declarations
    prosumer = RoleDeclaration(arg_dict["prosumer_id"], 'Prosumer')
    buyer = RoleDeclaration(arg_dict["buyer_id"], 'Buyer')
    
    PROSUMER = prosumer.to_obj()
    BUYER = buyer.to_obj()

    energy = AssetDeclaration('energy', 'Energy', [
        DeclarationProp('amount_kw', arg_dict["energy_qnt"], 'Number'),
    ])

    ENERGY = energy.to_obj()
    VOLTAGE = f'"{arg_dict["voltage"]}"'

    evt_dispatch = EventDeclaration('evt_dispatch', 'DispatchEnergy', [
        DeclarationProp('energy', ENERGY, 'Energy'),
        DeclarationProp('dispatcher', PROSUMER, 'Role'),
        DeclarationProp('recipient', BUYER, 'Role'),
        DeclarationProp('voltage', VOLTAGE, 'Number')
    ])
    
    evt_pay = EventDeclaration('evt_pay', 'Pay', [
            DeclarationProp('amount', arg_dict["amount"], 'Number'),
            DeclarationProp('currency', f'Currency({arg_dict["currency"]})', 'Currency'),
            DeclarationProp('from', BUYER, 'Role'),
            DeclarationProp('to', PROSUMER, 'Role')
        ])

    evt_pay_interest = EventDeclaration('evt_pay_interest', 'PayInterest', [
            DeclarationProp('amount', f'"(1 + {arg_dict["percentage"]} / 100) * {arg_dict["amount"]}"', 'Number'),
            DeclarationProp('currency', f'Currency({arg_dict["currency"]})', 'Currency'),
            DeclarationProp('from', BUYER, 'Role'),
            DeclarationProp('to', PROSUMER, 'Role')
        ])
    
    
    EVT_DISPATCH = evt_dispatch.to_obj()
    EVT_PAY = evt_pay.to_obj()
    EVT_PAY_INTEREST = evt_pay_interest.to_obj()

    # Declarations
    declarations = {
        'prosumer': prosumer,
        'buyer': buyer,
        'energy': energy,
        'evt_dispatch': evt_dispatch,
        'evt_pay': evt_pay,
        'evt_pay_interest': evt_pay_interest
    }


    # Contract Spec
    contract_spec = ContractSpec(
        'TransactiveEnergy',
        parameters = parameters,
        declarations = declarations,
        obligations = {
            'ob_dispatch': Obligation(
                'ob_dispatch',
                None,
                PROSUMER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_DISPATCH)
                )
            ),
            'ob_payment': Obligation(
                'ob_payment',
                None,
                BUYER,
                PROSUMER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_PAY)
                )
            ),
            'ob_pay_interest': Obligation(
                'ob_pay_interest',
                None,
                BUYER,
                PROSUMER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_PAY_INTEREST)
                )
            )
        },


        surviving_obligations = {
        },

        powers = {
            'pow_terminate_contract': Power(
                'pow_terminate_contract',
                None,
                BUYER,
                PROSUMER,
                PropMaker.make_default(),
                PFContract(PFContractName.Terminated)
            )
        }
    )

    return contract_spec
