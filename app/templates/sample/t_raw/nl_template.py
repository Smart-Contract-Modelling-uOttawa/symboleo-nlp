from app.classes.nl_template import NLTemplate, TemplateObj

sample_nl_template = NLTemplate(
    template_dict = {
        'delivery': TemplateObj(
            'The Seller shall deliver the Order in one delivery to the Buyer before (delivery_due_date).',
            ['obligations.delivery']
        ),
        'payment': TemplateObj(
            'The Buyer shall pay (payment_amount) to the Seller before (payment_due_date).',
            ['obligations.payment']
        ),
        'latePayment': TemplateObj(
            'In the event of late payment of the amount owed due, the Buyer shall pay interests equal to (interest_amount) percent of the payment amount.',
            ['obligations.latePayment']
        ),
        'disclosure': TemplateObj(
            'Both Seller and Buyer must keep the contents of this contract confidential for [CONFIDENTIALITY_MONTHS] months following the termination of the contract.',
            ['surviving_obligations.so1', 'surviving_obligations.so2']
        ),
        'suspendResumeDelivery': TemplateObj(
            'If payment is not completed, the Seller may suspend performance of all of its obligations under the agreement until payment is completed.',
            ['powers.suspendDelivery', 'powers.resumeDelivery']
        ),
        'terminateContract': TemplateObj(
            'Any delay in delivery of the goods will not entitle the Buyer to terminate the Contract unless delivery of goods is not completed.',
            ['powers.terminateContract']
        ),
    }
)


