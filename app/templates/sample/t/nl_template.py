from app.classes.nl_template import NLTemplate, TemplateObj

sample_nl_template = NLTemplate(
    template_dict = {
        'delivery': TemplateObj(
            'The Seller shall deliver the Order in one delivery to the Buyer',
            ['obligations.ob_delivery']
        ),
        'payment': TemplateObj(
            'The Buyer shall pay (payment_amount) to the Seller',
            ['obligations.ob_payment']
        ),
        'latePayment': TemplateObj(
            'The Buyer shall pay interests equal to (interest_amount) percent of the payment amount',
            ['obligations.ob_late_payment']
        ),
        'disclosure': TemplateObj(
            'Both Seller and Buyer must keep the contents of this contract confidential',
            ['surviving_obligations.so1', 'surviving_obligations.so2']
        ),
        'suspendDelivery': TemplateObj(
            'The Seller may suspend performance of all of its obligations under the agreement',
            ['powers.pow_suspend_delivery']
        ),
    }
)
