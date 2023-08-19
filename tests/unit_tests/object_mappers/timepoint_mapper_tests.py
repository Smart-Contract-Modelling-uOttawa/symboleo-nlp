import unittest
from unittest.mock import MagicMock

from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName
from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV
from app.classes.spec.sym_point import PointAtomContractEvent, PointVDE
from app.src.object_mappers.timepoint_mapper import TimepointMapper

class TimepointMapperTests(unittest.TestCase):
    def setUp(self):
        self.sut = TimepointMapper()

    def test_timepoint_mapper(self):
        result = self.sut.map(VariableEvent('evt_test'))
        self.assertEqual(result, PointVDE('evt_test.start'))

        result = self.sut.map(ContractEvent(ContractEventName.Activated))
        self.assertEqual(result, PointAtomContractEvent(ContractEvent(ContractEventName.Activated)))


if __name__ == '__main__':
    unittest.main()
