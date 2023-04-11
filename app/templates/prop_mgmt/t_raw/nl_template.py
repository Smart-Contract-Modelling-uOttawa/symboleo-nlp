from app.classes.spec.nl_template import NLTemplate, TemplateObj

nl_template = NLTemplate(
    template_dict = {
        # Could break this up...
        'advertise': TemplateObj(
            'The Manager shall advertise the Property for rent, engage and screen potential renters, enter into rental agreement(s) with acceptable renter(s).',
            ['obligations.ob_advertise']
        ),
        'reimburse': TemplateObj(
            'The Owner shall reimburse the Manager for all expenses related to such Advertising. ',
            ['obligations.ob_reimburse']
        ),
        'notify_expense': TemplateObj(
            'The Manager shall notify the Owner, in advance, of anticipated expenses related to such Advertising.',
            ['obligations.ob_notify_expense']
        ),
        'collect_rent': TemplateObj(
            'The Manager shall be responsible for all collection of Rent earned on the Property.',
            ['obligations.ob_collect_rent']
        ),
        'disbursement': TemplateObj(
            'The Manager shall then be responsible for disbursement of those proceeds to the Owner.',
            ['obligations.ob_disbursement']
        ),
        'accounting': TemplateObj(
            'The Manager shall further prepare and provide to the Owner a detailed accounting of all rents, expenses, and disbursements.',
            ['obligations.ob_accounting']
        ),
        'repair': TemplateObj(
            'The Manager shall be responsible for performing, or hiring necessary personnel to perform, all necessary maintenance and repairs to the Property. ',
            ['obligations.ob_repair']
        ),
        'reimburse_maintenance': TemplateObj(
            'The Owner shall reimburse the Manager for the cost of all such maintenance and repairs. ',
            ['obligations.ob_reimburse_maintenance']
        ),
        'repair_invoice': TemplateObj(
            'The Manager shall provide the Owner invoices of the actual costs.',
            ['obligations.ob_repair_invoice']
        ),
        'legal_proceedings': TemplateObj(
            'In the event that collection and/or legal proceedings become necessary with regard to the rental of the Property, The Manager shall handle all such proceedings.',
            ['obligations.ob_legal_proceedings']
        ),
        'termination_notice': TemplateObj(
            'This Agreement may be terminated at any time by either Party upon X days written notice to the other Party. ',
            ['powers.pow_terminate_notice_owner', 'powers.pow_terminate_notice_manager']
        ),
        'disburse_termination': TemplateObj(
            'Upon termination, the Manager shall disburse to the Owner any monies in the Manager\'s possession due and owing to the Owner within {DISBURSEMENT_DAYS=3-} days from the date of termination. ',
            ['obligations.ob_disburse_termination']
        ),
        'reimburse_termination': TemplateObj(
            'The Owner shall reimburse the Manager for any expenses incurred or approved prior to the date of termination within {REIMBURSEMENT_DAYS} days from the date of termination.',
            ['obligations.ob_reimburse_termination']
        )
    }
)


