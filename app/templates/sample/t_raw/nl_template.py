from app.classes.spec.nl_template import NLTemplate, TemplateObj

sample_nl_template = NLTemplate(
    template_dict = {
        'delivery': TemplateObj(
            'The Seller shall deliver the Order in one delivery to the Buyer before March 18, 2024.',
        ),
        'payment': TemplateObj(
            'The Buyer shall pay $100 CAD to the Seller before March 30, 2024.',
        ),
        'latePayment': TemplateObj(
            'In the event of late payment of the amount owed due, the Buyer shall pay interests equal to 8 percent of the payment amount.',
        ),
        'disclosure': TemplateObj(
            'Both Seller and Buyer must keep the contents of this contract confidential for 6 months following the termination of the contract.',
        ),
        # Tough one...
        'suspendDelivery': TemplateObj(
            'If payment is not completed, the Seller may suspend performance of all of its obligations under the agreement until payment is completed.',
            #['powers.pow_suspend_delivery', 'powers.pow_resume_ob_delivery']
        ),
        'terminateContract': TemplateObj(
            'Any delay in delivery of the goods will not entitle the Buyer to terminate the Contract unless delivery of goods is not completed.',
        ),
    }
)


