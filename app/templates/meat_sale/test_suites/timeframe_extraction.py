from tests_new.helpers.test_value import ContractSpecTestValue as TV

test_suite = [
    TV(
        input_value = 'within 2 weeks',
        expected_property = ['']
    ),
    TV(
        input_value = 'before April 25, 2022',
        expected_property = ['']
    ),
    TV(
        input_value = 'before the contract terminates',
        expected_property = ['']
    )
]
