import unittest
from unittest.mock import MagicMock

from app.classes.operations.user_input import UserInput
from app.classes.units.node_type import NodeType

from app.src.grammar.input_converter import InputConverter
from app.src.extractors.value_extractor import IExtractValue 

class ElementExtractorTests(unittest.TestCase):
    def setUp(self):
        self.fake_extractor = IExtractValue[str]()
        self.fake_extractor.extract = MagicMock(return_value = 'test')
        self.fake_dict = {
            NodeType.DUMMY: self.fake_extractor
        }
        self.sut = InputConverter(self.fake_dict)
    

    def test_element_extractor(self):
        user_input = [UserInput(NodeType.DUMMY, 'fake')]
        result = self.sut.convert(user_input)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].value, 'test')
        self.assertEqual(self.fake_extractor.extract.call_count, 1)


if __name__ == '__main__':
    unittest.main()
