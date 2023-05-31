from typing import Dict
from app.classes.spec.symboleo_contract import ContractSpec
from app.classes.spec.norm import Obligation, Power, SurvivingObligation
from app.classes.spec.prop_maker import PropMaker
from app.classes.spec.declaration import AssetDeclaration, EventDeclaration, RoleDeclaration, DeclarationProp
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.contract_spec_parameter import ContractSpecParameter as Parm
from app.classes.spec.other_predicates import *

arg_values = {
     'seller_id': 'seller',
     'seller_name': 'Shi Farms',
     'buyer_id': 'buyer',
     'buyer_name': 'Gridiron',
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

    seller = RoleDeclaration(arg_dict["seller_id"], 'Seller', [
        DeclarationProp('name', f'"{arg_dict["seller_name"]}"', 'String')
    ])
    buyer = RoleDeclaration(arg_dict["buyer_id"], 'Buyer', [
        DeclarationProp('name', f'"{arg_dict["buyer_name"]}"', 'String')
    ])
    legal_third_party = RoleDeclaration('third_party', 'ThirdParty', [
        DeclarationProp('name', '"third party"', 'String')
    ])
    SELLER = seller.to_obj()
    BUYER = buyer.to_obj()
    LEGAL_THIRD_PARTY = legal_third_party.to_obj()


    biomass = AssetDeclaration('biomass', 'Biomass', [
        DeclarationProp('quantity_lbs', arg_dict['biomass_quantity_lbs'], 'Number'),
        # Cannabidiol, THC, ... contaminants
    ])

    lab = AssetDeclaration('lab', 'Location', [
        DeclarationProp('name', '"lab"', 'String'),
    ])

    processor = AssetDeclaration('processor', 'Location', [
        DeclarationProp('name', '"processor"', 'String'),
    ])

    BIOMASS = biomass.to_obj()
    LAB = lab.to_obj()
    PROCESSOR = processor.to_obj()

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

    # evt_determine_analysis = EventDeclaration('evt_determine_analysis', 'DeterminesAnalysisRequired', [
    #     DeclarationProp('agent', BUYER, 'Role')
    # ])

    evt_delivery_lab = EventDeclaration('evt_delivery_lab', 'Delivery', [
        DeclarationProp('agent', SELLER, 'Role'),
        DeclarationProp('product', BIOMASS, 'Biomass'),
        DeclarationProp('location', LAB, 'Location'),
    ])

    evt_delivery_processor = EventDeclaration('evt_delivery_processor', 'Delivery', [
        DeclarationProp('agent', SELLER, 'Role'),
        DeclarationProp('product', BIOMASS, 'Biomass'),
        DeclarationProp('location', PROCESSOR, 'Location'),
    ])

    evt_legal_claim_buyer = EventDeclaration('evt_legal_claim_buyer', 'LegalClaim', [
        DeclarationProp('agent', LEGAL_THIRD_PARTY, 'Role'),
        DeclarationProp('target', BUYER, 'Role'),
    ])
    evt_legal_claim_seller = EventDeclaration('evt_legal_claim_seller', 'LegalClaim', [
        DeclarationProp('agent', LEGAL_THIRD_PARTY, 'Role'),
        DeclarationProp('target', SELLER, 'Role'),
    ])
    evt_legal_notice_buyer = EventDeclaration('evt_legal_notice_buyer', 'LegalNotice', [
        DeclarationProp('agent', LEGAL_THIRD_PARTY, 'Role'),
        DeclarationProp('target', BUYER, 'Role'),
    ])
    evt_legal_notice_seller = EventDeclaration('evt_legal_notice_seller', 'LegalNotice', [
        DeclarationProp('agent', LEGAL_THIRD_PARTY, 'Role'),
        DeclarationProp('target', SELLER, 'Role'),
    ])

    evt_return_info_buyer = EventDeclaration('evt_return_info_buyer', 'ReturnInfo', [
        DeclarationProp('agent', BUYER, 'Role')
    ])
    evt_return_info_seller = EventDeclaration('evt_return_info_seller', 'ReturnInfo', [
        DeclarationProp('agent', SELLER, 'Role')
    ])

    evt_disclose_info_buyer = EventDeclaration('evt_disclose_info_buyer', 'DiscloseInfo', [
        DeclarationProp('agent', BUYER, 'Role')
    ])
    evt_disclose_info_seller = EventDeclaration('evt_disclose_info_seller', 'DiscloseInfo', [
        DeclarationProp('agent', SELLER, 'Role')
    ])



    EVT_PAY = evt_pay.to_obj()
    EVT_QUARANTINE = evt_quarantine.to_obj()
    EVT_REMOVE_QUARANTINE = evt_remove_quarantine.to_obj()
    #EVT_DETERMINES_ANALYSIS_REQUIRED = evt_determine_analysis.to_obj()
    EVT_DELIVERY_LAB = evt_delivery_lab.to_obj()
    EVT_DELIVERY_PROCESSOR = evt_delivery_processor.to_obj()
    EVT_LEGAL_CLAIM_BUYER = evt_legal_claim_buyer.to_obj()
    EVT_LEGAL_NOTICE_BUYER = evt_legal_notice_buyer.to_obj()
    EVT_LEGAL_CLAIM_SELLER = evt_legal_claim_seller.to_obj()
    EVT_LEGAL_NOTICE_SELLER = evt_legal_notice_seller.to_obj()
    EVT_RETURN_INFO_BUYER = evt_return_info_buyer.to_obj()
    EVT_RETURN_INFO_SELLER = evt_return_info_seller.to_obj()
    EVT_DISCLOSE_INFO_BUYER = evt_disclose_info_buyer.to_obj()
    EVT_DISCLOSE_INFO_SELLER = evt_disclose_info_seller.to_obj()


    # Declarations
    declarations = {
        'seller': seller,
        'buyer': buyer,
        'third_party': legal_third_party,
        'biomass': biomass,
        'lab': lab,
        'processor': processor,
        'evt_pay': evt_pay,
        'evt_quarantine': evt_quarantine,
        'evt_remove_quarantine': evt_remove_quarantine,
        'evt_delivery_lab': evt_delivery_lab,
        'evt_delivery_processor': evt_delivery_processor,
        #'evt_determine_analysis': evt_determine_analysis,
        'evt_legal_claim_buyer': evt_legal_claim_buyer,
        'evt_legal_claim_seller': evt_legal_claim_seller,
        'evt_legal_notice_buyer': evt_legal_notice_buyer,
        'evt_legal_notice_seller': evt_legal_notice_seller,
        'evt_return_info_buyer': evt_return_info_buyer,
        'evt_return_info_seller': evt_return_info_seller,
        'evt_disclose_info_buyer': evt_disclose_info_buyer,
        'evt_disclose_info_seller': evt_disclose_info_seller
    }

    # Contract Spec
    contract_spec = ContractSpec(
        'Gridiron',
        parameters = parameters,
        declarations = declarations,
        preconditions = [
            # Shi Farms agrees to sell Product and Gridiron agrees to purchase 30,000 lbs. of hemp biomass ("Biomass") from Shi Farms.
            # Biomass must contain a minimum of six percent (6%) total Cannabidiol (CBD/and or CBDA) and all Biomass must have less than three percent (3%) total THC content.
            # The Biomass must contain no contaminates that are above acceptable industry standards for processing Biomass including but not limited to...
            # Both Parties agree that CBD potency numbers are determined by a third-party lab according to standard testing protocol which was provided by the seller.
        ],
        obligations = {
            'ob_payment': Obligation(
                'ob_payment',
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                # PropMaker.make(
                #     PredicateFunctionHappens(ContractEvent(ContractEventName.Activated))
                # ),
                PropMaker.make(PredicateFunctionHappens(EVT_PAY))
            ),

            'ob_quarantine': Obligation(
                'ob_quarantine',
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                #PropMaker.make(PredicateFunctionHappens(EVT_PAY)),
                PropMaker.make(PredicateFunctionHappens(EVT_QUARANTINE))
            ),

            'ob_keep_quarantine': Obligation(
                'ob_keep_quarantine',
                None,
                SELLER,
                BUYER,
                PropMaker.make(PredicateFunctionHappens(EVT_QUARANTINE)),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_REMOVE_QUARANTINE), negation=True
                )
                # PropMaker.make(
                #     PredicateFunctionWHappensBeforeEvent(
                #         EVT_REMOVE_QUARANTINE,
                #         EVT_DELIVERY_PROCESSOR
                #     ),
                #     negation=True
                # )
            ),

            'ob_delivery_lab': Obligation(
                'ob_delivery_lab',
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                #PropMaker.make(PredicateFunctionHappens(EVT_DETERMINES_ANALYSIS_REQUIRED)),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_DELIVERY_LAB)
                )
            ),

            'ob_delivery_processor': Obligation(
                'ob_delivery_processor',
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_DELIVERY_PROCESSOR)
                )
            ),

            'ob_legal_proceeding_buyer': Obligation(
                'ob_legal_proceeding_buyer',
                PropMaker.make(
                    PredicateFunctionHappens(EVT_LEGAL_CLAIM_BUYER)
                ),
                LEGAL_THIRD_PARTY,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_LEGAL_NOTICE_BUYER)
                )
            ),
            
            'ob_legal_proceeding_seller': Obligation(
                'ob_legal_proceeding_seller',
                PropMaker.make(
                    PredicateFunctionHappens(EVT_LEGAL_CLAIM_SELLER)
                ),
                LEGAL_THIRD_PARTY,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_LEGAL_NOTICE_SELLER)
                )
            ),

            'ob_return_info_buyer': Obligation(
                'ob_return_info_buyer',
                # PropMaker.make(
                #     PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))
                # ),
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_RETURN_INFO_BUYER)
                )
            ),
            'ob_return_info_seller': Obligation(
                'ob_return_info_seller',
                # PropMaker.make(
                #     PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))
                # ),
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_RETURN_INFO_SELLER)
                )
            ),
        },

        surviving_obligations = {
            'ob_disclose_info_buyer': SurvivingObligation(
                'ob_disclose_info_buyer',
                # PropMaker.make(
                #     PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))
                # ),
                None,
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_DISCLOSE_INFO_BUYER),
                    negation=True
                )
            ),
            'ob_disclose_info_seller': SurvivingObligation(
                'ob_disclose_info_seller',
                None,
                # PropMaker.make(
                #     PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))
                # ),
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(EVT_DISCLOSE_INFO_SELLER),
                    negation=True
                )
            ),
        },
        powers = {
            
        }
    )

    return contract_spec
