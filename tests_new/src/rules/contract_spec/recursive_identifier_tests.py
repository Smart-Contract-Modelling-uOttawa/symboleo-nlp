import unittest
from unittest.mock import MagicMock

from app.classes.spec.sym_point import PointFunction, PointVDE
from app.classes.spec.helpers import TimeUnitStr, TimeValueInt

from app.src.graph.graph_builder import GraphBuilder
from app.classes.spec.p_atoms import PAtom
from app.classes.processing.scored_components import ScoredComponent
from app.src.rules.contract_spec.dynamic_constructor import IConstructDynamicObjects, DynamicObjectConstructor
from app.src.rules.contract_spec.recursive_identifier import RecursiveParameterIdentifier

class PredicateScorerTests(unittest.TestCase):
    def setUp(self):
        graph_builder = GraphBuilder()
        self.graph = graph_builder.build(PAtom)
        
        id_dict = {
            'TimeUnitStr': lambda: TimeUnitStr('days'),
            'TimeValueInt': lambda: TimeValueInt(10),
            'PointVDE': lambda: PointVDE('test') 
        }

        self.dynamic_constructor = DynamicObjectConstructor(self.graph)

        self.sut = RecursiveParameterIdentifier(self.graph, self.dynamic_constructor)

    # These tests may need to be more focused. More DI
    def test_recursive_identifier(self):
        components = [
            TimeUnitStr('days'),
            TimeValueInt(10),
            PointVDE('test') 
        ]
        scored_components = [ScoredComponent(x,1) for x in components]
        

        result = self.sut.identify(PointFunction, scored_components)
        self.assertEqual(type(result.obj), PointFunction)
        self.assertEqual(result.score, 1)

        #self.assertEqual(self.dynamic_constructor.construct.call_count, 1)       

  
if __name__ == '__main__':
    unittest.main()