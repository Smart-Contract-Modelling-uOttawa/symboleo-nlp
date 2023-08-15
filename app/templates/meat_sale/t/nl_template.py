from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.parameter_config import ParameterConfig, PatternClassType

nl_template = NLTemplate(
    template_dict = {
        'delivery': TemplateObj(
            'The Seller shall deliver the Order in one delivery to the Buyer [P1]',
            {
                'P1': [ParameterConfig('obligations', 'ob_delivery', 'consequent')]
            }
        )
        ,
        'payment': TemplateObj(
            'The Buyer shall pay $100 to the Seller [P1]',
            {
                'P1': [ParameterConfig('obligations', 'ob_payment', 'consequent')]
            }
        ),
        'pay_interest': TemplateObj(
            '[P1] The Buyer shall pay interests equal to 8 percent of the payment amount',
            {
                'P1': [ParameterConfig('obligations', 'ob_late_payment', 'trigger')]
            }
        ),
        'disclosure': TemplateObj(
            'Both Seller and Buyer must keep the contents of this contract confidential [P1]',
            {
                'P1': [
                    ParameterConfig('surviving_obligations', 'so_disclosure_seller', 'consequent'),
                    ParameterConfig('surviving_obligations', 'so_disclosure_buyer', 'consequent')
                ]
            }
        ),
        'suspend_resume_delivery': TemplateObj(
            'In the event of late payment of the amount owed due, the Seller may suspend performance of all of its obligations under the agreement until payment of amounts owed has been received in full.',
        ),
        'terminate_contract': TemplateObj(
            'Any delay in delivery of the goods will not entitle the Buyer to terminate the Contract unless such delay exceeds 10 days.',
        ),
    }
)
