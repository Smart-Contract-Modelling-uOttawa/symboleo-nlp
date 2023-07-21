import unittest
from unittest.mock import MagicMock

from app.classes.operations.user_input import UserInput
from app.classes.units.unit_type import UnitType

from app.src.selection.element_extractor import ElementExtractor
from app.src.custom_event_extractor.element_extractor import IExtractElement 

class ElementExtractorTests(unittest.TestCase):
    def setUp(self):
        self.fake_extractor = IExtractElement[str]()
        self.fake_extractor.extract = MagicMock(return_value = 'test')
        self.fake_dict = {
            UnitType.DUMMY: self.fake_extractor
        }
        self.sut = ElementExtractor(self.fake_dict)
    

    def test_element_extractor(self):
        user_input = [UserInput(UnitType.DUMMY, 'fake')]
        result = self.sut.extract(user_input)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].value, 'test')
        self.assertEqual(self.fake_extractor.extract.call_count, 1)


if __name__ == '__main__':
    unittest.main()
