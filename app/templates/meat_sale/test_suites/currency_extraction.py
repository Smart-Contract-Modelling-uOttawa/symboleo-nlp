from tests_new.helpers.test_value import DomainPropTestValue as TV

test_suite = [
    TV(input_value = '$10.50 in USD', expected_property = ['USD']),
    TV(input_value = '$2000 USD', expected_property = ['USD']),
    TV(input_value = '500 CAD', expected_property = ['CAD']),
    TV(input_value = '$500.00 CAD', expected_property = ['CAD']),
    TV(input_value = 'USD 787', expected_property = ['USD'])
]
