from app.classes.spec.nl_template import NLTemplate, TemplateObj

nl_template = NLTemplate(
    template_dict = {
        'fee': TemplateObj(
            'The Contractor will charge the Client a flat fee of $100 for the Services (the "Compensation").'
        ),
        'invoice': TemplateObj(
            'The Client will be invoiced when the Services are complete.'
        ),
        'invoice_due': TemplateObj(
            'Invoices submitted by the Contractor to the Client are due within 10 days of receipt.'
        ),
        'partial_completion': TemplateObj(
            'In the event that this Agreement is terminated by the Client prior to completion of the Services, but where the Services have been partially performed, the Contractor will be entitled to pro rata payment of the Compensation to the date of termination provided that there has been no breach of contract on the part of the Contractor.'
        ),
        'reimburse': TemplateObj(
            'The Contractor will be reimbursed from time to time for reasonable and necessary expenses incurred by the Contractor in connection with providing the Services.'
        ),
        'disclose': TemplateObj(
            'The Contractor agrees that they will not disclose, divulge, reveal, report or use, for any purpose, any Confidential Information which the Contractor has obtained, except as authorized by the Client or as required by law.'
        ),

        # We've seen enough of these. Redundant
        # 'return_property': TemplateObj(
        #     'Upon the expiry or termination of this Agreement, the Contractor will return to the Client any property, documentation, records, or Confidential Information which is the property of the Client.'
        # ),
        
        'subcontract': TemplateObj(
            'Except as otherwise provided in this Agreement, the Contractor may, at the Contractor\'s absolute discretion, engage a third party sub-contractor to perform some or all of the obligations of the Contractor under this Agreement and the Client will not hire or engage any third parties to assist with the provision of the Services.'
        ),
        'subcontract_pay': TemplateObj(
            'the Contractor will pay the sub-contractor for its services and the Compensation will remain payable by the Client to the Contractor.'
        )
    }
)


