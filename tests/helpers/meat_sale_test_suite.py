from tests.helpers.test_unit import TestUnit

meat_sale_test_suite: list[TestUnit] = [
    TestUnit(
        'obligations', 
        'O1', 
        'trigger', 
        'the sky is blue', 
        'O1: occurs(is_blue(sky), X) => O(Seller, Buyer, T, happens(delivered, BEFORE delivered.delDueD))'
    ),
    ### Add more tests here...
]