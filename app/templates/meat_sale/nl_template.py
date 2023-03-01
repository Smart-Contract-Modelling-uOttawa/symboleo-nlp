from typing import Dict
from app.templates.template_classes import Parameter, PredicateProcessorConfig, DomainPropProcessorConfig, ContractParamType, DomainParamType, DomainParameter, ContractSpecParameter

nl_template = {
    'obligations': {
        'delivery': 'The Seller shall deliver the Order in one delivery to the Buyer [DELIVERY_REFINEMENT]',
        'delivery_old': 'The Seller shall deliver the Order in one delivery [DELIVERY_TIMEFRAME] to the Buyer [DELIVERY_LOCATION]',
        'payment': 'The Buyer shall pay [PAYMENT_DETAILS] to the Seller [PAYMENT_TIMEFRAME].',
        'latePayment': 'In the event of late payment of the amount owed due, the Buyer shall pay interests equal to [INTEREST_DETAILS]',
        'disclosure': 'Both Seller and Buyer must keep the contents of this contract confidential [CONFIDENTIALITY_TIMEFRAME]',
    },
    'powers': {
        # This refers to "all obligations" - may need to handle all of them...
        # The existence of suspendDelivery entails the existence of resumeDelivery. And it is initiated with a "Never" trigger
        'suspendResumeDelivery': '[DELIVERY_SUSPENSION_CONDITION] the Seller may suspend performance of all of its obligations under the agreement [DELIVERY_RESUMPTION_CONDITION]',
        'terminateContract': 'Any delay in delivery of the goods will not entitle the Buyer to terminate the Contract [TERMINATION_CONDITION]'
    }
}

sample_customization = [
    ('DELIVERY_TIMEFRAME', 'within 2 weeks'),
    ('DELIVERY_LOCATION', 'at the buyer\'s warehouse'),
    ('PAYMENT_DETAILS', '$100.00 CAD'),
    ('PAYMENT_TIMEFRAME', 'before April 17, 2022'),
    ('INTEREST_DETAILS', '10% of the amount owed'),
    ('CONFIDENTIALITY_TIMEFRAME', 'until 6 months after the termination of the contract'),
    ('DELIVERY_SUSPENSION_CONDITION', 'if payment is not made'),
    ('DELIVERY_RESUMPTION_CONDITION', 'until payment is made'),
    ('TERMINATION_CONDITION', 'unless such delay exceeds 10 Days')
]

parameters: Dict[str, Parameter] = {
    'DELIVERY_REFINEMENT': [
        # Shouldn't really need any of this stuff..
        ContractSpecParameter(
            ContractParamType.TIMEFRAME,
            PredicateProcessorConfig(
                norm_type = 'obligations',
                norm_id = 'delivery',
                norm_component = 'consequent',
            )
        )
    ],

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
                # 'location',
                # 'str'
            )
        )
    ],

    'PAYMENT_DETAILS': [
        DomainParameter(
            DomainParamType.AMOUNT,
            DomainPropProcessorConfig(
                'events',
                'paid',
                # 'amount',
                # 'str'
            )
        ),

        DomainParameter(
            DomainParamType.CURRENCY,
            DomainPropProcessorConfig(
                'events',
                'paid',
                # 'currency',
                # 'str'
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
                # 'amount',
                # 'str'
            )
        ),

        DomainParameter(
            DomainParamType.CURRENCY,
            DomainPropProcessorConfig(
                'events',
                'paidLate',
                # 'currency',
                # 'str'
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