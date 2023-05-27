import unittest
from unittest.mock import MagicMock

from app.classes.patterns.pattern import Pattern

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.declaration import Declaration
from app.classes.spec.domain_object import DomainObject
from app.classes.spec.norm import INorm
from app.classes.operations.contract_update_obj import ContractUpdateObj

from app.src.update_processor.domain_update_extractor import IExtractDomainUpdates, DomainUpdates
from app.src.update_processor.norm_update_extractor import IExtractNormUpdates
from app.src.update_processor.update_processor import UpdateProcessor

class UpdateProcessorTests(unittest.TestCase):
    def setUp(self):
        self.domain_update_extractor = IExtractDomainUpdates()

        fake_domain_update = DomainUpdates(
            [Declaration('a', 'b', 'c', [])],
            [DomainObject('a', 'b', [])]
        )
        self.domain_update_extractor.extract = MagicMock(return_value=fake_domain_update)

        self.norm_update_extractor = IExtractNormUpdates()
        self.norm_update_extractor.extract = MagicMock(return_value = [
            INorm()
        ])

        self.sut = UpdateProcessor(self.domain_update_extractor, self.norm_update_extractor)


    def test_update_processor(self):
        norm = INorm()
        pattern = Pattern()

        result = self.sut.process(norm, pattern)

        self.assertTrue(isinstance(result, ContractUpdateObj))
        self.assertEqual(len(result.declarations), 1)
        self.assertEqual(len(result.domain_objects), 1)
        self.assertEqual(len(result.norms), 1)
        self.assertEqual(self.domain_update_extractor.extract.call_count, 1)
        self.assertEqual(self.norm_update_extractor.extract.call_count, 1)

if __name__ == '__main__':
    unittest.main()
