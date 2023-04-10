from app.classes.nl_template import NLTemplate, TemplateObj

sample_nl_template = NLTemplate(
    template_dict = {
        'delivery': TemplateObj(
            'The Seller shall deliver the Order in one delivery to the Buyer before (delivery_due_date).',
            ['obligations.ob_delivery']
        ),
        'payment': TemplateObj(
            'The Buyer shall pay (payment_amount) to the Seller before (payment_due_date).',
            ['obligations.ob_payment']
        ),
        'latePayment': TemplateObj(
            'In the event of late payment of the amount owed due, the Buyer shall pay interests equal to (interest_amount) percent of the payment amount.',
            ['obligations.ob_late_payment']
        ),
        'disclosure': TemplateObj(
            'Both Seller and Buyer must keep the contents of this contract confidential for (confidentiality_months) months following the termination of the contract.',
            ['surviving_obligations.so1', 'surviving_obligations.so2']
        ),
        # Tough one...
        'suspendDelivery': TemplateObj(
            'If payment is not completed, the Seller may suspend performance of all of its obligations under the agreement until payment is completed.',
            ['powers.pow_suspend_delivery', 'powers.pow_resume_ob_delivery']
        ),
        'terminateContract': TemplateObj(
            'Any delay in delivery of the goods will not entitle the Buyer to terminate the Contract unless delivery of goods is not completed.',
            ['powers.pow_terminate_contract']
        ),
    }
)


