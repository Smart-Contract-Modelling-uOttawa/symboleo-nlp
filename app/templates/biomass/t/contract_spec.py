from typing import Dict
from app.classes.spec.symboleo_contract import ContractSpec
from app.classes.spec.norm import Obligation, Power, SurvivingObligation
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.declaration import AssetDeclaration, EventDeclaration, RoleDeclaration, DeclarationProp
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.contract_spec_parameter import ContractSpecParameter as Parm
from app.classes.spec.other_predicates import *
from app.classes.spec.sym_situation import ObligationState, ObligationStateName
from app.classes.spec.sym_event import ContractEvent, ContractEventName

arg_values = {
     'seller_id': 'shi_farms',
     'seller_name': 'Shi Farms',
     'buyer_id': 'gridiron',
     'buyer_name': 'GridIron',
     'biomass_quantity_lbs': 30000,
     'currency': 'USD',
     'price': 150000

}

def get_contract_spec(arg_dict: Dict[str,str] = arg_values):

    parameters = [
        Parm('seller_id', 'String'),
        Parm('seller_name', 'String'),
        Parm('buyer_id', 'String'),
        Parm('buyer_name', 'String'),
        Parm('biomass_quantity', 'Number'),
        Parm('price', 'Number'),
        Parm('currency', 'Currency'),
    ]

    shi_farms = RoleDeclaration(arg_dict["seller_name"], 'Seller', id=arg_dict["seller_id"], props=[
        DeclarationProp('name', f'"{arg_dict["seller_name"]}"', 'String')
    ])
    gridiron = RoleDeclaration(arg_dict["buyer_name"], 'Buyer', id=arg_dict["buyer_id"], props = [
        DeclarationProp('name', f'"{arg_dict["buyer_name"]}"', 'String')
    ])
    SELLER = shi_farms.to_obj()
    BUYER = gridiron.to_obj()

    biomass = AssetDeclaration('biomass', 'Biomass', [
        DeclarationProp('quantity_lbs', arg_dict['biomass_quantity_lbs'], 'Number'),
        # Cannabidiol, THC, ... contaminants
    ])

    lab = AssetDeclaration('lab', 'Location', [
        DeclarationProp('name', '"lab"', 'String'),
    ])

    BIOMASS = biomass.to_obj()
    LAB = lab.to_obj()

    evt_pay = EventDeclaration('evt_pay', 'Pay', [
        DeclarationProp('to', SELLER, 'Role'),
        DeclarationProp('from', BUYER, 'Role'),
        DeclarationProp('amount', arg_dict["price"], 'Role'),
        DeclarationProp('currency', f'Currency({arg_dict["currency"]})', 'Currency'),
    ])

    evt_quarantine = EventDeclaration('evt_quarantine', 'Quarantine', [
        DeclarationProp('agent', SELLER, 'Role'),
        DeclarationProp('product', BIOMASS, 'Biomass')
    ])

    evt_remove_quarantine = EventDeclaration('evt_remove_quarantine', 'RemoveQuarantine', [
        DeclarationProp('agent', SELLER, 'Role'),
        DeclarationProp('product', BIOMASS, 'Biomass')
    ])

    evt_delivery_lab = EventDeclaration('evt_delivery_lab', 'Delivery', [
        DeclarationProp('agent', SELLER, 'Role'),
        DeclarationProp('product', BIOMASS, 'Biomass'),
        DeclarationProp('location', LAB, 'Location'),
    ])



    EVT_PAY = evt_pay.to_obj()
    EVT_QUARANTINE = evt_quarantine.to_obj()
    EVT_REMOVE_QUARANTINE = evt_remove_quarantine.to_obj()
    EVT_DELIVERY_LAB = evt_delivery_lab.to_obj()


    # Declarations
    declarations = {
        'shi_farms': shi_farms,
        'gridiron': gridiron,
        'biomass': biomass,
        'lab': lab,
        'evt_pay': evt_pay,
        'evt_quarantine': evt_quarantine,
        'evt_remove_quarantine': evt_remove_quarantine,
        'evt_delivery_lab': evt_delivery_lab
    }

    # Contract Spec
    contract_spec = ContractSpec(
        'biomass',
        parameters = parameters,
        declarations = declarations,
        preconditions = [],
        postconditions = [],
        obligations = {
            'ob_payment': Obligation(
                'ob_payment',
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(PredicateFunctionHappens(EVT_PAY))
            ),

            'ob_quarantine': Obligation(
                'ob_quarantine',
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(PredicateFunctionHappens(EVT_QUARANTINE))
            ),

            'ob_keep_quarantine': Obligation(
                'ob_keep_quarantine',
                None,
                SELLER,
                BUYER,
                PropMaker.make(PredicateFunctionHappens(EVT_QUARANTINE)),
                PropMaker.make(
                    PredicateFunctionHappens(
                        EVT_REMOVE_QUARANTINE
                    ),
                    negation=True
                )
            ),

            'ob_delivery_lab': Obligation(
                'ob_delivery_lab',
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_DELIVERY_LAB)
                )
            ),

        },
        powers = {
        }
    )

    return contract_spec
