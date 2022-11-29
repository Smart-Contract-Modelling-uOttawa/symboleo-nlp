from tests_new.helpers.test_value import DomainPropTestValue as TV

test_suite = [
    TV(input_value = '$10.50 in USD', expected_property = ['10.50']),
    TV(input_value = '$2000 USD', expected_property = ['2000']),
    TV(input_value = '500 CAD', expected_property = ['500']),
    TV(input_value = '$555.55 CAD', expected_property = ['555.55']),
    TV(input_value = 'USD 787', expected_property = ['787'])
]
