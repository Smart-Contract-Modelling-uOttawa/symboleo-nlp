import unittest
from unittest.mock import MagicMock
from typing import Dict
from app.classes.operations.user_input import UnitType, UserInput
from app.classes.spec.declaration import Declaration
from app.classes.spec.domain_object import DomainObject

from app.src.nl_creator.nl_creator import NLCreator
from app.src.nl_creator.nl_fillers.nl_unit_filler import IFillNLUnit

class NLCreatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fake_filler = IFillNLUnit()
        self.fake_filler.fill = MagicMock(return_value=['aa', 'bb'])

        test_dict: Dict[UnitType, IFillNLUnit] = {
            UnitType.DUMMY: self.fake_filler
        } 

        self.sut = NLCreator(test_dict)


    def test_domain_update_extractor(self):
        input_list = [UserInput(UnitType.DUMMY, 'test value')]
        result = self.sut.create(input_list)
        self.assertEqual(result, 'aa bb')

        self.assertEqual(self.fake_filler.fill.call_count, 1)



if __name__ == '__main__':
    unittest.main()