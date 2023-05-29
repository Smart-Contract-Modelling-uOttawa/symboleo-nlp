from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.parameter_config import ParameterConfig

nl_template = NLTemplate(
    template_dict = {
        'delivery': TemplateObj(
            'The Seller shall deliver the Order in one delivery to the Buyer [P2]',
            {
                'P2': [ParameterConfig('obligations', 'ob_delivery', 'consequent')]
            }
        )
        ,
        'payment': TemplateObj(
            'The Buyer shall pay $100 to the Seller [P2]',
            {
                'P2': [ParameterConfig('obligations', 'ob_payment', 'consequent')]
            }
        ),
        'latePayment': TemplateObj(
            '[P1] The Buyer shall pay interests equal to 8 percent of the payment amount',
            {
                'P1': [ParameterConfig('obligations', 'ob_late_payment', 'trigger')]
            }
        ),
        'disclosure': TemplateObj(
            'Both Seller and Buyer must keep the contents of this contract confidential [P2]',
            {
                'P2': [
                    ParameterConfig('surviving_obligations', 'so_disclosure_seller', 'consequent'),
                    ParameterConfig('surviving_obligations', 'so_disclosure_buyer', 'consequent')
                ]
            }
        ),
        'suspendDelivery': TemplateObj(
            '[P1] The Seller may suspend performance of all of its obligations under the agreement [P2]',
            {
                'P1': [ParameterConfig('powers', 'pow_suspend_delivery', 'trigger')],
                'P2': [ParameterConfig('powers', 'pow_suspend_delivery', 'consequent')]
            }
        ),
    }
)
