from tests_new.helpers.test_value import DomainPropTestValue as TV

test_suite = [
    TV(input_value = 'at the warehouse', expected_property = ['buyer.warehouse']),
    TV(input_value = 'to the warehouse', expected_property = ['buyer.warehouse']),
    TV(input_value = 'at their warehouse', expected_property = ['buyer.warehouse']),
    TV(input_value = 'at the location', expected_property = ['buyer.warehouse']),
    TV(input_value = 'at their location', expected_property = ['buyer.warehouse']), 
    TV(input_value = 'at their address', expected_property = ['seller.address']),
    TV(input_value = 'at its warehouse', expected_property = ['buyer.warehouse']),
    TV(input_value = 'at the buyer\'s warehouse', expected_property = ['buyer.warehouse']),
    TV(input_value = 'at the buyer\'s address', expected_property = ['buyer.warehouse']),
    TV(input_value = 'at 883 5th Ave, Ottawa, ON', expected_property = ['buyer.address'])
    # Need to handle addresses...
]
