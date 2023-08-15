from app.classes.spec.nl_template import NLTemplate, TemplateObj

nl_template = NLTemplate(
    template_dict = {
        'delivery': TemplateObj(
            'The Seller shall deliver the Order in one delivery to the Buyer before March 18, 2024.',
        ),
        'payment': TemplateObj(
            'The Buyer shall pay $100 to the Seller before March 30, 2024.',
        ),
        'pay_interest': TemplateObj(
            'In the event of late payment of the amount owed due, the Buyer shall pay interests equal to 8 percent of the payment amount.',
        ),
        'disclosure': TemplateObj(
            'Both Seller and Buyer must keep the contents of this contract confidential for 6 months following the termination of the contract.',
        ),
        'suspend_resume_delivery': TemplateObj(
            'In the event of late payment of the amount owed due, the Seller may suspend performance of all of its obligations under the agreement until payment of amounts owed has been received in full.',
        ),
        'terminate_contract': TemplateObj(
            'Any delay in delivery of the goods will not entitle the Buyer to terminate the Contract unless such delay exceeds 10 days.',
        ),
    }
)


