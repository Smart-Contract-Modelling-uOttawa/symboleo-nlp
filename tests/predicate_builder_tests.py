import unittest
from unittest.mock import MagicMock, call
from app.classes.spec.primitive import Primitive
from app.src.dynamic_constructor import IConstructDynamicObjects
from app.src.primitive_checker import ICheckPrimitives
from app.src.predicate_builder import PredicateBuilder
from tests.helpers.test_graph import TestGraph

class FakePrimitiveChecker(ICheckPrimitives):
    def check(self, name: str, primitives: list[Primitive]):
        return name in ['e', 'f']

class PredicateBuilderTests(unittest.TestCase):
    def setUp(self):
        self.digraph = TestGraph.get_digraph()

    def test_primitive_checks(self):
        primitive_checker = ICheckPrimitives()
        primitive_checker.check = MagicMock(return_value = None)

        dynamic_constructor = IConstructDynamicObjects()
        dynamic_constructor.construct = MagicMock(return_value = None)
        
        sut = PredicateBuilder(self.digraph, primitive_checker, dynamic_constructor)

        result = sut.build('a', [])
        primitive_check_calls = [call(x, []) for x in ['e','e','f','f','g']]
        primitive_checker.check.assert_has_calls(primitive_check_calls, any_order=True)
        dynamic_constructor.construct.assert_not_called()


    def test_dynamic_constructor(self):
        primitive_checker = FakePrimitiveChecker()
        dynamic_constructor = IConstructDynamicObjects()
        dynamic_constructor.construct = MagicMock(return_value = True)
        sut = PredicateBuilder(self.digraph, primitive_checker, dynamic_constructor)

        result = sut.build('c', [])
        self.assertTrue(result)
        dc_calls = [call('c', [True, True])]
        dynamic_constructor.construct.assert_has_calls(dc_calls)

    
  
if __name__ == '__main__':
    unittest.main()