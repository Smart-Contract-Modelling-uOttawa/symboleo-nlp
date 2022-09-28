from tests.helpers.test_unit import TestUnit

meat_sale_obligation_test_suite: list[TestUnit] = [
    TestUnit(
        'obligations', 
        'delivery', 
        'trigger', 
        'the sky is blue', 
        'delivery: Happens(is_blue(sky)) -> O(seller, buyer, true, WhappensBefore(delivered, delivered.delDueDate))'
    ),

    TestUnit(
        'obligations',
        'latePayment',
        'trigger',
        'the cat is angry',
        'latePayment: Happens(Violated(obligations.payment)) AND Happens(is_angry(cat)) -> O(buyer, seller, true, Happens(paidLate))'
    )
    ### Add more tests here...
]