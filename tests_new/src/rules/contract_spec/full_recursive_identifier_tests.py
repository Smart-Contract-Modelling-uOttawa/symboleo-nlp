import unittest
from unittest.mock import MagicMock

from tests.helpers.test_nlp import TestNLP
from app.classes.spec.sym_point import PointFunction, PointVDE
from app.classes.spec.helpers import TimeUnitStr, TimeValueInt

from app.src.rules.contract_spec.all_primitive_scorer_builder import get_identifiers
from app.src.graph.graph_builder import GraphBuilder
from app.classes.spec.p_atoms import PAtom
from app.src.rules.contract_spec.dynamic_constructor import IConstructDynamicObjects, DynamicObjectConstructor
from app.src.rules.contract_spec.recursive_identifier import RecursiveParameterIdentifier

# Fix these tests
test_suite = [
    (
        PointFunction,
        'within 2 weeks'
    )
]

class PredicateScorerTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        graph_builder = GraphBuilder()
        self.graph = graph_builder.build(PAtom)
        
        id_dict = get_identifiers(self.nlp)

        self.dynamic_constructor = DynamicObjectConstructor(self.graph)

        self.sut = RecursiveParameterIdentifier(self.graph, id_dict, self.dynamic_constructor)

    # These tests may need to be more focused. More DI
    def test_recursive_identifier_full(self):
        
        for target_type, text in test_suite:
            doc = self.nlp(text,)
            result = self.sut.identify(doc, target_type)
            print(result)
            self.assertEqual(type(result.obj), target_type)
  

  
if __name__ == '__main__':
    unittest.main()