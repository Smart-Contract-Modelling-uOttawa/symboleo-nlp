import unittest
from unittest.mock import MagicMock

from app.src.operations.dependency_builder import DependencyBuilder, Dependencies

class DependencyBuilderTests(unittest.TestCase):

    def test_contract_updater(self):
        x = DependencyBuilder.build(fake=True)
        self.assertEqual(type(x), Dependencies)


if __name__ == '__main__':
    unittest.main()
