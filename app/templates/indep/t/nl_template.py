from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.parameter_config import ParameterConfig

nl_template = NLTemplate(
    template_dict = {
        'fee': TemplateObj(
            'The Contractor will charge the Client a flat fee of $100 for the Services (the "Compensation").'
        ),
        # when the Services are complete
        'invoice': TemplateObj(
            'The Client will be invoiced [P1].',
            {
                'P1': [ParameterConfig('obligations', 'ob_invoice', 'trigger')]
            }
        ),
        # within 10 days of receipt
        'invoice_due': TemplateObj(
            'Invoices submitted by the Contractor to the Client are due [P1].',
            {
                'P1': [ParameterConfig('obligations', 'ob_invoice_due', 'consequent')]
            }
        ),

        # In the event that this Agreement is terminated by the Client prior to completion of the Services
        # provided that there has been no breach of contract on the part of the Contractor
        # but where the Services have been partially performed
        'partial_completion': TemplateObj(
            '[P1] the Contractor will be entitled to pro rata payment of the Compensation to the date of termination.',
            {
                'P1': [ParameterConfig('obligations', 'ob_partial_completion', 'antecedent')]
            }
        ),

        'reimburse': TemplateObj(
            'The Contractor will be reimbursed from time to time for reasonable and necessary expenses incurred by the Contractor in connection with providing the Services.'
        ),

        # except/unless...
        'disclose': TemplateObj(
            'The Contractor agrees that they will not disclose, divulge, reveal, report or use, for any purpose, any Confidential Information which the Contractor has obtained, [P1]',
            {
                'P1': [ParameterConfig('obligations', 'ob_not_disclose', 'trigger')]
            }
        ),

        # only taking the client non-obligation part        
        'subcontract': TemplateObj(
            'Except as otherwise provided in this Agreement, the Contractor may, at the Contractor\'s absolute discretion, engage a third party sub-contractor to perform some or all of the obligations of the Contractor under this Agreement and the Client will not hire or engage any third parties to assist with the provision of the Services.'
        ),
        'subcontract_pay': TemplateObj(
            'the Contractor will pay the sub-contractor for its services and the Compensation will remain payable by the Client to the Contractor.'
        )
    }
)


