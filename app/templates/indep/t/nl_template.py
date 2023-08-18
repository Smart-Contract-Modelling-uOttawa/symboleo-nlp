from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.parameter_config import ParameterConfig

nl_template = NLTemplate(
    template_dict = {
        # when the Services are complete
        'send_invoice': TemplateObj(
            'The Client will be invoiced [P1].',
            {
                'P1': [ParameterConfig('obligations', 'ob_send_invoice', 'trigger')]
            }
        ),
        # within 10 days of receipt
        'pay_invoice': TemplateObj(
            'Invoices submitted by the Contractor to the Client are due [P1].',
            {
                'P1': [ParameterConfig('obligations', 'ob_pay_invoice', 'consequent')]
            }
        ),

        # In the event that this Agreement is terminated by the Client prior to completion of the Services
        # provided that there has been no breach of contract on the part of the Contractor
        # but where the Services have been partially performed
        'partial_completion': TemplateObj(
            'In the event that this Agreement is terminated prior to completion of the Services, but where the Services have been partially performed, the Contractor will be entitled to pro rata payment of the Compensation to the date of termination [P1].',
            {
                'P1': [ParameterConfig('obligations', 'ob_partial_completion', 'antecedent')]
            }
        ),

        'reimburse_expenses': TemplateObj(
            'The Contractor will be reimbursed from time to time for reasonable and necessary expenses incurred by the Contractor in connection with providing the Services.'
        ),

        # except/unless...
        'disclose': TemplateObj(
            'The Contractor agrees that they will not disclose, divulge, reveal, report or use, for any purpose, any Confidential Information which the Contractor has obtained [P1]',
            {
                'P1': [ParameterConfig('obligations', 'ob_not_disclose', 'trigger')]
            }
        ),

    }
)


