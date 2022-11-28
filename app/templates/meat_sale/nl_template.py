from app.templates.template_classes import PredicateProcessorConfig, DomainPropProcessorConfig, ContractParamType, DomainParamType, DomainParameter, ContractSpecParameter

nl_template = {
    'obligations': {
        'delivery': 'The Seller shall deliver the Order in one delivery [DELIVERY_TIMEFRAME] to the Buyer [DELIVERY_LOCATION]',
        'payment': 'The Buyer shall pay [PAYMENT_DETAILS] to the Seller [PAYMENT_TIMEFRAME].',
        'latePayment': 'In the event of late payment of the amount owed due, the Buyer shall pay interests equal to [INTEREST_DETAILS]'
    }
}

sample_customization = [
    ('DELIVERY_TIMEFRAME', 'within 2 weeks'),
    ('DELIVERY_LOCATION', 'at the buyer\'s warehouse'),
    ('PAYMENT_DETAILS', '$100.00 CAD'),
    ('PAYMENT_TIMEFRAME', 'before April 17, 2022'),
    ('INTEREST_DETAILS', '10% of the amount owed')
]

parameters = {
    'DELIVERY_TIMEFRAME': [
        ContractSpecParameter(
            ContractParamType.TIMEFRAME,
            PredicateProcessorConfig(
                norm_type = 'obligations',
                norm_id = 'delivery',
                norm_component = 'consequent',
            )
        )
    ],

    'DELIVERY_LOCATION': [
        DomainParameter(
            DomainParamType.LOCATION,
            DomainPropProcessorConfig(
                'events',
                'delivered',
                'location',
                'str'
            )
        )
    ],

    'PAYMENT_DETAILS': [
        DomainParameter(
            DomainParamType.AMOUNT,
            DomainPropProcessorConfig(
                'events',
                'paid',
                'amount',
                'str'
            )
        ),

        DomainParameter(
            DomainParamType.CURRENCY,
            DomainPropProcessorConfig(
                'events',
                'paid',
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
                norm_id = 'payment',
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
}