from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.parameter_config import ParameterConfig

nl_template = NLTemplate(
    template_dict = {
        'sell_buy': TemplateObj(
            'Shi Farms agrees to sell Product and Gridiron agrees to purchase 30,000 lbs. of hemp biomass ("Biomass") from Shi Farms.',
            #[]
        ),
        'biomass_contents': TemplateObj(
            'Biomass must contain a minimum of six percent (6%) total Cannabidiol (CBD/and or CBDA) and all Biomass must have less than three percent (3%) total THC content.',
            #[]
        ),
        'contaminants': TemplateObj(
            'The Biomass must contain no contaminates that are above acceptable industry standards for processing Biomass including but not limited to: Mold and Mildew; Non-Hemp Plant Material; Soil; Insects; Rodent Droppings; Wet or Rotting Material; Heavy Metals; Residual Pesticides or Herbicides; Bacteria.',
            #[]
        ),
        'pricing': TemplateObj(
            'Both Parties mutually agree that the Purchase Price of the Product is determined on a $5.00 per pound basis for a total cost of one hundred fifty thousand dollars ($150,000).',
            #[]
        ),
        'lab_testing': TemplateObj(
            'Both Parties agree that CBD potency numbers are determined by a third-party lab according to standard testing protocol which was provided by the seller.',
            #[]
        ),
        'buyer_testing': TemplateObj(
            'Buyer may take their own samples ("Product Samples") for testing as well.',
            #[]
        ),
        'payment': TemplateObj(
            '[P1] Both Parties agree that once the Parties have agreed to transaction which includes the purchase and sale of the Product that the Buyer will remit payment [PARAMETER]',
            #['obligations.ob_payment']
            {
                'P1': [ParameterConfig('obligations', 'ob_payment', 'trigger')],
            }
        ),
        'quarantine': TemplateObj( 
            'Once the payment has been received, Shi Farms will use its best efforts to quarantine product to ensure safe keeping of the Product until delivery date as agreed by the Parties.',
            #[
                #'obligations.ob_quarantine'
            #]
        ),
        'delivery_location': TemplateObj(
            '[P1] The point of delivery of the Product Samples shall be a laboratory determined by Gridiron',
            #['obligations.ob_delivery_lab']
            {
                'P1': [ParameterConfig('obligations', 'ob_delivery_lab', 'trigger')],
            }
        ),
        'shipping': TemplateObj(
            'Shi Farms shall be responsible to ship the Product Samples to the designated laboratory.',
            #['obligations.ob_delivery_lab']
        ),
        'delivery': TemplateObj(
            'Shi Farms shall be responsible for delivery of the Biomass to the processor determined by Gridiron, in good form as described above "A. Product".',
            #['obligations.ob_delivery_processor']
        ),
        'termination': TemplateObj(
            'Either Party may terminate this Agreement at any time prior to delivery of the Product.',
            #['powers.pow_termination_buyer', 'powers.pow_termination_seller']
        ),
        'legal_proceeding': TemplateObj(
            '[P1] prompt notice is required by the one to the other.', # Coreference on "one" - what to do? maybe replace manually
            #['obligations.ob_legal_proceeding_buyer', 'obligations.ob_legal_proceeding_seller']
            {
                'P1': [
                    ParameterConfig('obligations', 'ob_legal_proceeding_buyer', 'trigger'),
                    ParameterConfig('obligations', 'ob_legal_proceeding_seller', 'trigger')
                ]
            }
        ),
        'return_disclose_info': TemplateObj(
            '[P1] each party shall return all copies of any such information to the other and take every reasonable measure to preclude its representatives from sharing or keeping such information.',
            # [
            #     'obligations.ob_return_info_buyer', 
            #     'obligations.ob_return_info_seller', 
            #     'surviving_obligations.ob_disclose_info_buyer',
            #     'surviving_obligations.ob_disclose_info_seller'
            # ]
            {
                'P1': [
                    ParameterConfig('obligations', 'ob_return_info_buyer', 'trigger'),
                    ParameterConfig('obligations', 'ob_return_info_seller', 'trigger'),
                    ParameterConfig('surviving_obligations', 'ob_disclose_info_buyer', 'trigger'),
                    ParameterConfig('surviving_obligations', 'ob_disclose_info_seller', 'trigger')
                ]
            }
        ) 
    }
)


# Severability, indemnification, governing law, amendment, confidential information...


