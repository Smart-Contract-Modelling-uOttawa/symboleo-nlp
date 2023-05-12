from app.classes.spec.nl_template import NLTemplate, TemplateObj
from app.classes.spec.parameter_config import ParameterConfig

rental_nl_template = NLTemplate(
    template_dict = {
        'pay_rent': TemplateObj(
            'The monthly rent to be paid by the Renter to the Landlord is (monthly_rent). It is to be paid by the Renter before the first day of every month, such that the first rent payment is due on (first_rent_due_date).',
            #['obligations.ob_pay_rent']
            # Will probably add a refinement here... need to figure out frequency
        ),
        'late_payment': TemplateObj(
            '[P1] The Landlord is entitled to impose a (late_fine) fine as late fee',
            #['obligations.ob_late_payment']
            {
                'P1': [ParameterConfig('obligations', 'ob_late_payment', 'trigger')]
            }
        ),
        'pay_security_deposit': TemplateObj(
            'The Renter will pay the Landlord an amount of (security_deposit_amount) as a security deposit to cover the cost of any damages suffered by the premises and cleaning [P2]',
            #['obligations.ob_pay_security_deposit']
            {
                'P2': [ParameterConfig('obligations', 'ob_pay_security_deposit', 'consequent')]
            }
        ),
        'return_deposit': TemplateObj(
            '[P1] Such security deposit will be returned to the Renter, provided the premises are left in the same condition as prior to the occupancy [P2]',
            #['obligations.ob_return_deposit']
            {
                'P1': [ParameterConfig('obligations', 'ob_return_deposit', 'trigger')],
                'P2': [ParameterConfig('obligations', 'ob_return_deposit', 'consequent')]
            }
            # Might add further antecedents...?
        ),
        'no_pets': TemplateObj(
            '[P1] The Parties agree that the Renter will not keep any pets on the premises [P2]',
            #['obligations.ob_no_pets'] 
            {
                'P1': [ParameterConfig('obligations', 'ob_no_pets', 'trigger')],
                'P2': [ParameterConfig('obligations', 'ob_no_pets', 'consequent')]
            }
        ),
        
        ## Remove all absolute termination powers
        # 'terminate_notice': TemplateObj(
        #     'This Agreement may be terminated in the event that any of the following occurs: 2. At any given time [TERMINATION_CONDITION2]',
        #     ['powers.terminate_notice']
        # ),
        # 'terminate_abandon': TemplateObj(
        #     '[TERMINATION_CONDITION3], the Landlord will be entitled to enter the Premises by any means without facing any liability and the Landlord may terminate this Agreement.',
        #     ['powers.terminate_abandon']
        # )
    }
)
