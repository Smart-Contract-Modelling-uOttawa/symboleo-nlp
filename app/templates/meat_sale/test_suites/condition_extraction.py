from tests_new.helpers.test_value import ContractSpecTestValue as TV

test_suite = [
    TV(
        input_value = 'if payment is not made',
        expected_sym = ['Happens(Violated(obligations.payment))'],
        key='DELIVERY_SUSPENSION_CONDITION'
    ),

    TV(
        input_value = 'until payment is made',
        expected_sym = ['HappensWithin(paidLate, Suspension(obligations.delivery))'],
        key='DELIVERY_RESUMPTION_CONDITION'
    ),


    # TV(
    #     input_value = 'until 6 months after termination of the contract',
    #     expected_sym = ['WhappensBefore(test, Date.add(activated(self), 6, months))']
    # ),
    # TV(
    #     input_value = 'before the contract terminates',
    #     expected_sym = ['WhappensBeforeE(test, contract.terminates)'] # Currently failing
    # ),
    
]
