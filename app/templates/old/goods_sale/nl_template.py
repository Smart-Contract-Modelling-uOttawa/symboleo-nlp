from app.templates.template_classes import PredicateProcessorConfig, DomainPropProcessorConfig, ContractParamType, DomainParamType, DomainParameter, ContractSpecParameter

nl_template = {
    'obligations': {
        'sellGoods': 'The seller hereby agrees to sell the Goods to the Customer [PAYMENT_DETAILS]',
        'provideInvoice': 'The seller will provide an invoice to the customer [INVOICE_TIMEFRAME]',
        'payInvoice': 'All invoices are to be paid in full [PAYMENT_TIMEFRAME]',
        'LateFee': 'Any balances not paid [PAYMENT_TIMEFRAME] will be subject to a 5% late payment penalty',
    },
    'powers': {
        'terminateContract': 'This agreement may be terminated by either party or both parties at any instant provided that the terminating party provides a written notice of termination [TERMINATION_TIMEFRAME]'
    }
}

sample_customization = [
    ('SALES_AMOUNT', 'for an amount of $100 CAD'),
    ('INVOICE_TIMEFRAME', 'at the time of delivery'),
    ('PAYMENT_TIMEFRAME', 'within 30 days'),
    ('TERMINATION_TIMEFRAME', '10 days in advance')
]

# TODO:
parameters = {
    'PAYMENT_DETAILS': [
        DomainParameter(
            DomainParamType.AMOUNT,
            DomainPropProcessorConfig(
                'events',
                'payInvoice',
                'amount',
                'str'
            )
        ),

        DomainParameter(
            DomainParamType.CURRENCY,
            DomainPropProcessorConfig(
                'events',
                'payInvoice',
                'currency',
                'str'
            )
        )
    ],

    'PAYMENT_TIMEFRAME': [
        ContractSpecParameter(
            ContractParamType.TIMEFRAME,
            PredicateProcessorConfig(
                norm_type = 'obligations',
                norm_id = 'pay',
                norm_component = 'consequent',
            )
        )
    ],

    'INTEREST_DETAILS': [
        DomainParameter(
            DomainParamType.AMOUNT,
            DomainPropProcessorConfig(
                'events',
                'paidLate',
                'amount',
                'str'
            )
        ),

        DomainParameter(
            DomainParamType.CURRENCY,
            DomainPropProcessorConfig(
                'events',
                'paidLate',
                'currency',
                'str'
            )
        )
    ],

    'CONFIDENTIALITY_TIMEFRAME': [
        ContractSpecParameter(
            ContractParamType.TIMEFRAME,
            PredicateProcessorConfig(
                norm_type = 'obligations',
                norm_id = 'disclosure1',
                norm_component = 'consequent',
            )
        ),
        ContractSpecParameter(
            ContractParamType.TIMEFRAME,
            PredicateProcessorConfig(
                norm_type = 'obligations',
                norm_id = 'disclosure2',
                norm_component = 'consequent',
            )
        )
    ],

    'DELIVERY_SUSPENSION_CONDITION': [
        ContractSpecParameter(
            ContractParamType.CONDITION,
            PredicateProcessorConfig(
                norm_type = 'powers',
                norm_id = 'suspendDelivery',
                norm_component = 'trigger',
            )
        )
    ],

    'DELIVERY_RESUMPTION_CONDITION': [
        ContractSpecParameter(
            ContractParamType.CONDITION,
            PredicateProcessorConfig(
                norm_type = 'powers',
                norm_id = 'resumeDelivery',
                norm_component = 'trigger',
            )
        )
    ],

    'TERMINATION_CONDITION': [
        ContractSpecParameter(
            ContractParamType.CONDITION,
            PredicateProcessorConfig(
                norm_type = 'powers',
                norm_id = 'terminateContract',
                norm_component = 'trigger'
            )
        )
    ]
}