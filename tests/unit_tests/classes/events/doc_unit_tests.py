import unittest
from unittest.mock import MagicMock

from app.classes.events.doc_unit import DocUnit, NlpDoc

class DocUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        x = 0
    
    def test_doc_unit(self):
        x = NlpDoc([
            DocUnit('a', 'a', 'a', 'a')
        ])

        y = NlpDoc([
            DocUnit('a', 'a', 'a', 'a')
        ])

        self.assertEqual(x, y)


if __name__ == '__main__':
    unittest.main()