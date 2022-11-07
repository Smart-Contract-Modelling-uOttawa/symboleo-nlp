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
    {
        'sentence': 'Payment was received after the due date',
        'primitives': [
            ObligationEvent('fulfilled', 'payment'),
            VariableDotExpression('delivered.delDueDate')
        ]
    },
    {
        'sentence': 'The seller terminates the agreement before delivery of goods',
        'primitives': [
            ContractEvent('terminated'),
            VariableDotExpression('delivery')
        ]
    },
    {
        'sentence': 'The meat is of poorer quality than agreed upon.'
    },
    {
        'sentence': 'The payment has been completed.'
    },
    {
        'sentence': 'The payment has not been received.'
    },
    {
        'sentence': 'The meat was delivered a day late'
    },
    {
        'sentence': 'The meat was delivered on time'
    },
    {
        'sentence': 'Delivery was paused by the seller'
    },
    {
        'sentence': 'The seller failed to deliver the goods.'
    },
    {
        'sentence': 'The goods were delivered'
    },
    {
        'sentence': 'Delivery has not been resumed'
    }
]
