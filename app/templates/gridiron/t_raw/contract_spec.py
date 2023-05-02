from app.classes.spec.symboleo_contract import ContractSpec
from app.classes.spec.norm import Obligation, Power, SurvivingObligation
from app.classes.spec.prop_maker import PropMaker
from app.classes.spec.predicate_function import *
from app.classes.spec.power_function import *
from app.classes.spec.contract_spec_parameter import ContractSpecParameter
from app.classes.spec.other_predicates import *
from app.classes.spec.proposition import PAnd, PComparison, PEquality, Proposition, PNegAtom, PAtomStringLiteral, PComparisonOp
from app.classes.spec.sym_situation import ObligationState, ObligationStateName
from app.classes.spec.sym_event import ContractEvent, ContractEventName
from app.src.helpers.declarer import Declarer

from app.templates.gridiron.t_raw.domain_model import get_domain_model

def get_contract_spec():
    dm = get_domain_model()

    SELLER = 'seller'
    BUYER = 'buyer'
    THIRD_PARTY = 'third_party'

    parameters = [
        ContractSpecParameter('buyer', 'Buyer'),
        ContractSpecParameter('seller', 'Seller'),
        ContractSpecParameter('third_party', 'ThirdParty'),
        ContractSpecParameter('v_quantity', 'Number'),
        ContractSpecParameter('v_cannabidiol_percent', 'Number'),
        ContractSpecParameter('v_thc_percent', 'Number'),
        ContractSpecParameter('v_currency', 'Currency'),
        ContractSpecParameter('v_shipping_location', 'String'),
    ]

    # Creating the objects
    seller = Declarer.declare(dm, 'roles', 'Seller', 'seller', [
        ('name', 'Shi Farms')
    ])
    buyer = Declarer.declare(dm, 'roles', 'Buyer', 'buyer', [
        ('name', 'Gridiron')
    ])
    third_party = Declarer.declare(dm, 'roles', 'ThirdParty', 'third_party', [
        ('name', 'Legal Third Party')
    ])

    biomass = Declarer.declare(dm, 'assets', 'Biomass', 'biomass', [
        ('quantity', 'v_quantity'),
        ('cannabidiol_percent', 'v_cannabidiol_percent'),
        ('thc_percent', 'v_thc_percent'),
    ])

    evt_payment = Declarer.declare(dm, 'events', 'Payment', 'evt_payment', [
        ('agent', BUYER),
        ('receiver', SELLER),
        ('amount', 'v_amount'),
        ('currency', 'v_currency'),
    ])
    evt_quarantine = Declarer.declare(dm, 'events', 'Quarantine', 'evt_quarantine', [
        ('product', 'biomass')
    ])
    evt_delivery_lab = Declarer.declare(dm, 'events', 'Delivery', 'evt_delivery_lab', [
        ('from', SELLER),
        ('to', BUYER),
        ('product', 'biomass'),
        ('location', 'lab specified by Gridiron'), 
    ])
    evt_delivery_processor = Declarer.declare(dm, 'events', 'Delivery', 'evt_delivery_processor', [
        ('from', SELLER),
        ('to', BUYER),
        ('product', 'biomass'),
        ('location', 'processor'),
    ])
    evt_determines_analysis = Declarer.declare(dm, 'events', 'DeterminesAnalysis', 'evt_determines_analysis', [
        ('agent', BUYER)
        # This will be more complicated
    ])
    evt_legal_claim_buyer = Declarer.declare(dm, 'events', 'LegalClaim', 'evt_legal_claim_buyer', [
        ('agent', THIRD_PARTY),
        ('target', BUYER),
    ])
    evt_legal_claim_seller = Declarer.declare(dm, 'events', 'LegalClaim', 'evt_legal_claim_seller', [
        ('agent', THIRD_PARTY),
        ('target', SELLER),
    ])
    evt_legal_notice_buyer = Declarer.declare(dm, 'events', 'LegalNotice', 'evt_legal_notice_buyer', [
        ('agent', THIRD_PARTY),
        ('receiver', BUYER)
    ])
    evt_legal_notice_seller = Declarer.declare(dm, 'events', 'LegalNotice', 'evt_legal_notice_seller', [
        ('agent', THIRD_PARTY),
        ('receiver', SELLER)
    ])
    evt_return_info_buyer = Declarer.declare(dm, 'events', 'ReturnInfo', 'evt_return_info_buyer', [
        ('agent', BUYER), 
        ('receiver', SELLER)
    ])
    evt_return_info_seller = Declarer.declare(dm, 'events', 'ReturnInfo', 'evt_return_info_seller', [
        ('agent', SELLER),
        ('receiver', BUYER)
    ])
    evt_disclose_info_buyer = Declarer.declare(dm, 'events', 'DiscloseInfo', 'evt_disclose_info_buyer', [
        ('agent', BUYER)
    ])
    evt_disclose_info_seller = Declarer.declare(dm, 'events', 'DiscloseInfo', 'evt_disclose_info_seller', [
        ('agent', SELLER)
    ])

    # Declarations
    declarations = {
        'seller': seller,
        'buyer': buyer,
        'third_party': third_party,
        'biomass': biomass,
        'evt_payment': evt_payment,
        'evt_quarantine': evt_quarantine,
        'evt_delivery_lab': evt_delivery_lab,
        'evt_delivery_processor': evt_delivery_processor,
        'evt_determines_analysis': evt_determines_analysis,
        'evt_legal_claim_buyer': evt_legal_claim_buyer,
        'evt_legal_claim_seller': evt_legal_claim_seller,
        'evt_legal_notice_buyer': evt_legal_notice_buyer,
        'evt_legal_notice_seller': evt_legal_notice_seller,
        'evt_return_info_buyer': evt_return_info_buyer,
        'evt_return_info_seller': evt_return_info_seller,
        'evt_disclose_info_buyer': evt_disclose_info_buyer,
        'evt_disclose_info_seller': evt_disclose_info_seller
    }

    # Variables to use
    BIOMASS = biomass.to_obj()
    PAYMENT = evt_payment.to_obj()
    QUARANTINE = evt_quarantine.to_obj()
    DELIVERY_LAB = evt_delivery_lab.to_obj()
    DELIVERY_PROCESSOR = evt_delivery_processor.to_obj()
    DETERMINES_ANALYSIS = evt_determines_analysis.to_obj()
    LEGAL_CLAIM_BUYER = evt_legal_claim_buyer.to_obj()
    LEGAL_CLAIM_SELLER = evt_legal_claim_seller.to_obj()
    LEGAL_NOTICE_BUYER = evt_legal_notice_buyer.to_obj()
    LEGAL_NOTICE_SELLER = evt_legal_notice_seller.to_obj()
    RETURN_INFO_BUYER = evt_return_info_buyer.to_obj()
    RETURN_INFO_SELLER = evt_return_info_buyer.to_obj()
    DISCLOSE_INFO_BUYER = evt_disclose_info_buyer.to_obj()
    DISCLOSE_INFO_SELLER = evt_disclose_info_seller.to_obj()

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
        postconditions = [
        ],
        obligations = {
            'ob_payment': Obligation(
                'ob_payment',
                PropMaker.make(
                    PredicateFunctionHappens(ContractEvent(ContractEventName.Activated))
                ),
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(PAYMENT)
                )
            ),
            
            ## Unhandled - need a way to represent the SITUATION of quarantining
            # 'ob_quarantine': Obligation(
            #     'ob_quarantine',
            #     PropMaker.make(PredicateFunctionHappens(PAYMENT)),
            #     SELLER,
            #     BUYER,
            #     PropMaker.make_default(),
            #     PropMaker.make(
            #         PredicateFunctionOccurs(...)
            #     )
            # ),

            'ob_delivery_lab': Obligation(
                'ob_delivery_lab',
                PropMaker.make(PredicateFunctionHappens(DETERMINES_ANALYSIS)),
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(DELIVERY_LAB)
                )
            ),

            'ob_delivery_processor': Obligation(
                'ob_delivery_processor',
                None,
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(DELIVERY_PROCESSOR)
                )
            ),

            'ob_legal_proceeding_buyer': Obligation(
                'ob_legal_proceeding_buyer',
                PropMaker.make(
                    PredicateFunctionHappens(LEGAL_CLAIM_BUYER)
                ),
                THIRD_PARTY,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(LEGAL_NOTICE_BUYER)
                )
            ),
            'ob_legal_proceeding_seller': Obligation(
                'ob_legal_proceeding_seller',
                PropMaker.make(
                    PredicateFunctionHappens(LEGAL_CLAIM_SELLER)
                ),
                THIRD_PARTY,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(LEGAL_NOTICE_SELLER)
                )
            ),

            'ob_return_info_buyer': Obligation(
                'ob_return_info_buyer',
                PropMaker.make(
                    PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))
                ),
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(RETURN_INFO_BUYER)
                )
            ),
            'ob_return_info_seller': Obligation(
                'ob_return_info_seller',
                PropMaker.make(
                    PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))
                ),
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(RETURN_INFO_SELLER)
                )
            ),
        },

        surviving_obligations = {
            'ob_disclose_info_buyer': Obligation(
                'ob_disclose_info_buyer',
                PropMaker.make(
                    PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))
                ),
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(DISCLOSE_INFO_BUYER),
                    negation=True
                )
            ),
            'ob_disclose_info_seller': Obligation(
                'ob_disclose_info_seller',
                PropMaker.make(
                    PredicateFunctionHappens(ContractEvent(ContractEventName.Terminated))
                ),
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PropMaker.make(
                    PredicateFunctionHappens(DISCLOSE_INFO_SELLER),
                    negation=True
                )
            ),
        },
        powers = {
            'pow_termination_buyer': Power(
                'pow_termination_buyer',
                None, 
                BUYER,
                SELLER,
                PropMaker.make_default(),
                PFContract(PFContractName.Terminated)
            ),
            'pow_termination_seller': Power(
                'pow_termination_seller',
                None, 
                SELLER,
                BUYER,
                PropMaker.make_default(),
                PFContract(PFContractName.Terminated)
            ),
            ## Need PFPower implemented...
            # 'pow_suspend_termination_buyer': Power(
            #     PropMaker.make(
            #         PredicateFunctionHappens(DELIVERY_PROCESSOR)
            #     ),
            #     SELLER,
            #     BUYER,
            #     PropMaker.make_default(),
            #     PFPower(PFPowerName.Cancelled, 'pow_termination_buyer')
            # ),
            # 'pow_suspend_termination_seller': Power(
            #     PropMaker.make(
            #         PredicateFunctionHappens(DELIVERY_PROCESSOR)
            #     ),
            #     SELLER,
            #     BUYER,
            #     PropMaker.make_default(),
            #     PFPower(PFPowerName.Cancelled, 'pow_termination_seller')
            # )
        },
        constraints = [
        ]
    )

    return contract_spec
