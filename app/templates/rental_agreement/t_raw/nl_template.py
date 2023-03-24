from typing import Dict, List
from app.src.operations.parm_operations.configs import ParameterConfig, ParameterSpec, ParmOpCode
from app.classes.nl_template import NLTemplate, TemplateObj

rental_nl_template = NLTemplate(
    template_dict = {
        'pay_rent': TemplateObj(
            'The monthly rent to be paid by the Renter to the Landlord is (monthly_rent). It is to be paid by the Renter before the first day of every month, such that the first rent payment is due on (first_rent_due_date).',
            ['obligations.pay_rent']
        ),
        'late_payment': TemplateObj(
            'In the event of late payments made by the Renter, the Landlord is entitled to impose a (late_fine) fine as late fee. ',
            ['obligations.late_payment']
        ),
        'pay_security_deposit': TemplateObj(
            'Prior to taking occupancy of the premises, the Renter will pay the Landlord an amount of (security_deposit_amount) as a security deposit to cover the cost of any damages suffered by the premises and cleaning.',
            ['obligations.pay_security_deposit']
        ),
        'return_deposit': TemplateObj(
            'Such security deposit will be returned to the Renter upon the end of this Agreement, provided the premises are left in the same condition as prior to the occupancy.',
            ['obligations.return_deposit']
        ),
        'no_pets': TemplateObj(
            'The Parties agree that the Renter will not keep any pets on the premises without obtaining written prior consent from the Landlord.',
            ['obligations.no_pets', 'powers.allow_pets'] # Does this make sense...?
        ),
        'terminate_breach': TemplateObj(
            'This Agreement may be terminated in the event that any of the following occurs: 1. Immediately in the event that one of the Parties breaches this Agreement.',
            ['powers.terminate_breach1', 'powers.terminate_breach2']
        ),
        'terminate_notice': TemplateObj(
            'This Agreement may be terminated in the event that any of the following occurs: 2. At any given time by providing written notice to the other party (termination_notice_days) days prior to terminating the Agreement.',
            ['powers.terminate_notice']
        ),
        'terminate_abandon': TemplateObj(
            'In the event that the Renter abandons the premises during the term of this Agreement, the Landlord will be entitled to enter the Premises by any means without facing any liability and the Landlord may terminate this Agreement.',
            ['powers.terminate_abandon']
        )

    }
)
