from app.classes.spec.nl_template import NLTemplate, TemplateObj

rental_nl_template = NLTemplate(
    template_dict = {
        'pay_rent': TemplateObj(
            'The monthly rent to be paid by the Renter to the Landlord is (monthly_rent). It is to be paid by the Renter before the first day of every month, such that the first rent payment is due on (first_rent_due_date).',
            ['obligations.ob_pay_rent']
            # Will probably add a refinement here... need to figure out frequency
        ),
        'late_payment': TemplateObj(
            'The Landlord is entitled to impose a (late_fine) fine as late fee. ',
            ['obligations.ob_late_payment']
        ),
        'pay_security_deposit': TemplateObj(
            'The Renter will pay the Landlord an amount of (security_deposit_amount) as a security deposit to cover the cost of any damages suffered by the premises and cleaning.',
            ['obligations.ob_pay_security_deposit']
        ),
        'return_deposit': TemplateObj(
            'Such security deposit will be returned to the Renter, provided the premises are left in the same condition as prior to the occupancy.',
            ['obligations.ob_return_deposit']
            # Might add further antecedents...?
        ),
        'no_pets': TemplateObj(
            'The Parties agree that the Renter will not keep any pets on the premises.',
            ['obligations.ob_no_pets'] 
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
