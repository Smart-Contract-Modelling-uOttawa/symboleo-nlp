import unittest
from unittest.mock import MagicMock
from app.classes.patterns.pattern_classes import PatternClass
from app.classes.operations.handle_object import HandleObject

from app.classes.spec.norm import INorm

from app.src.norm_update_extractor.norm_update_extractor import NormUpdateExtractor
from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates

from tests.helpers.test_objects import CustomEvents

class NormUpdateExtractorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fake_handler = IHandleNormUpdates()
        self.fake_handler.handle = MagicMock(return_value = [INorm()])
        handler_dict = {PatternClass: self.fake_handler }
        self.sut = NormUpdateExtractor(
            handler_dict
        )

    def test_norm_update_extractor(self):
        pattern = PatternClass()
        handle_obj = HandleObject(INorm())

        result = self.sut.extract(pattern, handle_obj)

        self.assertEqual(len(result), 1)
        self.assertEqual(self.fake_handler.handle.call_count, 1)


if __name__ == '__main__':
    unittest.main()