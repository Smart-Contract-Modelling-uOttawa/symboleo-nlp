import unittest
from unittest.mock import MagicMock

from app.src.operations.dependency_builder import DependencyBuilder
from app.classes.operations.user_input import UserInput
from app.classes.spec.norm import Obligation
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionSHappensBefore
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE

from app.classes.units.all_units import *

from app.classes.operations.contract_update_obj import ContractUpdateObj

from app.src.update_processor2.operation_mapper_builder import OperationMapperBuilder
from app.src.update_processor2.operation_mapper import OperationMapper

from tests.helpers.test_contract import get_test_contract_for_assets

class UpdateProcessorTests(unittest.TestCase):
    def setUp(self):
        deps = DependencyBuilder.build(fake=True)
        self.sut = OperationMapperBuilder.build(deps)

    def test_update_processor(self):
        test_input = [
            UserInput(UnitType.BEFORE),
            UserInput(UnitType.DATE, 'March 30, 2024')
        ]

        contract = None

        norm = Obligation(
            'ob_test', 
            None, 
            'partyA', 
            'partyB',
            PropMaker.make_default(), 
            PropMaker.make(
                PredicateFunctionHappens(VariableEvent('evt_init'))
            )
        )

        expected_norm = Obligation(
            'ob_test', 
            None, 
            'partyA', 
            'partyB',
            PropMaker.make_default(), 
            PropMaker.make(
                PredicateFunctionSHappensBefore(VariableEvent('evt_init'), Point(PointVDE('"March 30, 2024"')))
            )
        )

        result = self.sut.map(test_input, contract, norm)

        self.assertTrue(isinstance(result, ContractUpdateObj))
        self.assertEqual(len(result.declarations), 0)
        self.assertEqual(len(result.domain_objects), 0)
        self.assertEqual(len(result.norms), 1)
        self.assertEqual(result.norms[0], expected_norm)
    
    def test_update_processor2(self):
        test_input = [
            UserInput(UnitType.WITHIN),
            UserInput(UnitType.TIMESPAN, '2 weeks'),
            UserInput(UnitType.OF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT),
            UserInput(UnitType.SUBJECT, 'renter'),
            UserInput(UnitType.VERB, 'occupying'),
            UserInput(UnitType.DOBJ, 'the property'),
        ]

        contract = get_test_contract_for_assets()

        norm = Obligation(
            'ob_test', 
            None, 
            'renter', 
            'manager',
            PropMaker.make_default(), 
            PropMaker.make(
                PredicateFunctionHappens(VariableEvent('evt_payment'))
            )
        )


        result = self.sut.map(test_input, contract, norm)

        self.assertTrue(isinstance(result, ContractUpdateObj))
        self.assertEqual(len(result.declarations), 2)
        self.assertEqual(len(result.domain_objects), 2)
        self.assertEqual(len(result.norms), 1)

        print(result.norms[0].to_sym())
        
        
        #self.assertEqual(result.norms[0], expected_norm)


if __name__ == '__main__':
    unittest.main()
