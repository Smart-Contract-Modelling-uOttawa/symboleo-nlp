from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.parameter_config import ParameterConfig

sample_nl_template = NLTemplate(
    template_dict = {
        'delivery': TemplateObj(
            'The Seller shall deliver the Order in one delivery to the Buyer [P2]',
            {
                'P2': [ParameterConfig('obligations', 'ob_delivery', 'consequent')]
            }
        )
        ,
        'payment': TemplateObj(
            'The Buyer shall pay (payment_amount) to the Seller [P2]',
            {
                'P2': [ParameterConfig('obligations', 'ob_payment', 'consequent')]
            }
        ),
        'latePayment': TemplateObj(
            '[P1] The Buyer shall pay interests equal to (interest_amount) percent of the payment amount',
            {
                'P1': [ParameterConfig('obligations', 'ob_late_payment', 'trigger')]
            }
        ),
        'disclosure': TemplateObj(
            'Both Seller and Buyer must keep the contents of this contract confidential [P2]',
            {
                'P2': [
                    ParameterConfig('surviving_obligations', 'so1', 'consequent'),
                    ParameterConfig('surviving_obligations', 'so2', 'consequent')
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
