from tests_new.helpers.test_value import ContractSpecTestValue as TV

test_suite = [
    TV(
        input_value = 'within 2 weeks',
        expected_sym = ['WhappensBefore(test, Date.add(activated(self), 2, weeks))']
    ),
    TV(
        input_value = 'before April 25, 2022',
        expected_sym = ['WhappensBefore(test, April 25, 2022)']
    ),
    TV(
        input_value = 'until 6 months after termination of the contract',
        expected_sym = ['WhappensBefore(test, Date.add(activated(self), 6, months))']
    ),
    TV(
        input_value = 'before the contract terminates',
        expected_sym = ['WhappensBeforeE(test, contract.terminates)']
    )
]
