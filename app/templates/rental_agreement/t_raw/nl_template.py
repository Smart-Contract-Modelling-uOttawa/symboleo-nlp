
from app.classes.spec.nl_template import NLTemplate, TemplateObj

rental_nl_template = NLTemplate(
    template_dict = {
        'pay_rent': TemplateObj(
            'The monthly rent to be paid by the Renter to the Landlord is (monthly_rent). It is to be paid by the Renter before the first day of every month, such that the first rent payment is due on (first_rent_due_date).',
            ['obligations.ob_pay_rent']
        ),
        'late_payment': TemplateObj(
            'In the event of late payments made by the Renter, the Landlord is entitled to impose a (late_fine) fine as late fee. ',
            ['obligations.ob_late_payment']
        ),
        'pay_security_deposit': TemplateObj(
            'Prior to taking occupancy of the premises, the Renter will pay the Landlord an amount of (security_deposit_amount) as a security deposit to cover the cost of any damages suffered by the premises and cleaning.',
            ['obligations.ob_pay_security_deposit']
        ),
        'return_deposit': TemplateObj(
            'Such security deposit will be returned to the Renter upon the end of this Agreement, provided the premises are left in the same condition as prior to the occupancy.',
            ['obligations.ob_return_deposit']
        ),
        'no_pets': TemplateObj(
            'The Parties agree that the Renter will not keep any pets on the premises without obtaining written prior consent from the Landlord.',
            ['obligations.ob_no_pets', 'powers.pow_suspend_ob_no_pets'] # Does this make sense...?
        ),
        'terminate_notice': TemplateObj(
            'This Agreement may be terminated in the event that any of the following occurs: 2. At any given time by providing written notice to the other party (termination_notice_days) days prior to terminating the Agreement.',
            ['powers.pow_termination_written']
        ),
        'terminate_abandon': TemplateObj(
            'In the event that the Renter abandons the premises during the term of this Agreement, the Landlord will be entitled to enter the Premises by any means without facing any liability and the Landlord may terminate this Agreement.',
            ['powers.pow_termination_abandon']
        )

    }
)
