from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.parameter_config import ParameterConfig

nl_template = NLTemplate(
    template_dict = {
        'pay_rent': TemplateObj(
            'The monthly rent to be paid by the Renter to the Landlord is $1500. It is to be paid by the Renter before the first day of every month, such that the first rent payment is due on March 1, 2024.'
        ),
        
        'late_payment': TemplateObj(
            '[P1] The Landlord is entitled to impose a $50 fine as late fee',
            {
                'P1': [ParameterConfig('obligations', 'ob_late_payment', 'antecedent')]
            }
        ),
        
        'pay_security_deposit': TemplateObj(
            'The Renter will pay the Landlord an amount of $1000 as a security deposit to cover the cost of any damages suffered by the premises and cleaning [P2]',
            {
                'P2': [ParameterConfig('obligations', 'ob_pay_deposit', 'consequent')]
            }
        ),
        
        'return_deposit': TemplateObj(
            '[P1] Such security deposit will be returned to the Renter, provided the premises are left in the same condition as prior to the occupancy',
            {
                'P1': [ParameterConfig('obligations', 'ob_return_deposit', 'antecedent')]
            }
        ),

        'no_pets': TemplateObj(
            'The Parties agree that the Renter will not keep any pets on the premises [P2]', 
            {
                'P2': [ParameterConfig('obligations', 'ob_no_pets', 'consequent')]
            }
        ),

        'terminate_notice': TemplateObj(
            'This Agreement may be terminated in the event that any of the following occurs: 2. At any given time by providing written notice to the other party 30 days prior to terminating the Agreement.'
        ),
        
        'terminate_abandon': TemplateObj(
            '[P1] the Landlord may terminate this Agreement.',
            {
                'P1': [ParameterConfig('powers', 'terminate_abandon', 'consequent')]
            }
        )
    }
)
