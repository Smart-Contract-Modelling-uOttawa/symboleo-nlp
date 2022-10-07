from app.classes.spec.sym_event import ContractEvent, ObligationEvent
from app.classes.spec.helpers import VariableDotExpression

# Make a class for these...
## Or just put an expected object and define equality operators...

full_test_suite = [
    {
        'sentence': 'Delivery of goods has been completed',
        'primitives': [
            ObligationEvent('fulfilled', 'delivery')
        ]
    },
    {
        'sentence': 'The buyer failed to make late payments',
        'primitives': [
            ObligationEvent('violated', 'latePayment')
        ]
    },
    # {
    #     'sentence': 'Payment was received after the due date',
    #     'primitives': [
    #         ObligationEvent('fulfilled', 'payment'),
    #         VariableDotExpression('delivered.delDueDate')
    #     ]
    # },
    # {
    #     'sentence': 'The seller terminates the agreement before delivery of goods',
    #     'spec': 'HappensBefore(Terminated(self))'
    # }
]