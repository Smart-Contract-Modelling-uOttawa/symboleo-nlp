
from app.classes.spec.nl_template import NLTemplate, TemplateObj

nl_template = NLTemplate(
    template_dict = {
        'pay_rent': TemplateObj(
            'The monthly rent to be paid by the Renter to the Landlord is $1500. It is to be paid by the Renter before the first day of every month, such that the first rent payment is due on March 1, 2024.'
        ),
        'late_payment': TemplateObj(
            'In the event of late payments made by the Renter, the Landlord is entitled to impose a $50 fine as late fee. '
        ),
        'pay_security_deposit': TemplateObj(
            'Prior to taking occupancy of the premises, the Renter will pay the Landlord an amount of $1000 as a security deposit to cover the cost of any damages suffered by the premises and cleaning.'
        ),
        'return_deposit': TemplateObj(
            'Such security deposit will be returned to the Renter upon the end of this Agreement, provided the premises are left in the same condition as prior to the occupancy.'
        ),
        'no_pets': TemplateObj(
            'The Parties agree that the Renter will not keep any pets on the premises without obtaining written prior consent from the Landlord.'
        ),
        'terminate_notice': TemplateObj(
            'This Agreement may be terminated in the event that any of the following occurs: 2. At any given time by providing written notice to the other party 30 days prior to terminating the Agreement.'
        ),
        'terminate_abandon': TemplateObj(
            'In the event that the Renter abandons the premises during the term of this Agreement, the Landlord may terminate this Agreement.'
        )

    }
)
