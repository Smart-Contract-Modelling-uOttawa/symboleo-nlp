import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.declaration import Declaration
from app.classes.spec.contract_spec_parameter import ContractSpecParameter
from app.classes.spec.domain_object import DomainObject
from app.classes.spec.norm import INorm
from app.classes.pattern_classes.pattern_class import PatternClass
from app.classes.operations.contract_update_obj import ContractUpdateObj

from app.src.operations.operation_mapper import OperationMapper
from app.src.operations.pattern_class_resolver import IResolvePatternClasses
from app.src.pattern_builder.pattern_class_builder import IBuildPatternClass
from app.src.norm_update_extractor.norm_update_extractor import IExtractNormUpdates
from app.src.domain_update_extractor.domain_update_extractor import IExtractDomainUpdates, DomainUpdates

class OperationMapperTests(unittest.TestCase):
    def setUp(self):

        self.pattern_class_builder = IBuildPatternClass()
        fake_pattern_class = PatternClass()
        self.pattern_class_builder.build = MagicMock(return_value=[fake_pattern_class])

        self.pattern_class_resolver = IResolvePatternClasses()
        self.pattern_class_resolver.resolve = MagicMock(return_value=fake_pattern_class)

        self.domain_update_extractor = IExtractDomainUpdates()

        fake_domain_update = DomainUpdates(
            [Declaration('a', 'b', 'c', [])],
            [DomainObject('a', 'b', [])],
            [ContractSpecParameter('a','b')]
        )
        self.domain_update_extractor.extract = MagicMock(return_value=fake_domain_update)

        self.norm_update_extractor = IExtractNormUpdates()
        self.norm_update_extractor.extract = MagicMock(return_value = [
            INorm()
        ])

        self.sut = OperationMapper(
            self.pattern_class_builder,
            self.pattern_class_resolver,
            self.norm_update_extractor,
            self.domain_update_extractor
        )

    def test_operation_mapper(self):
        test_input = [
        ]
        contract = ISymboleoContract()
        norm = INorm()

        result = self.sut.map(test_input, contract, norm)

        self.assertTrue(isinstance(result, ContractUpdateObj))
        self.assertEqual(len(result.declarations), 1)
        self.assertEqual(len(result.domain_objects), 1)
        self.assertEqual(len(result.norms), 1)
        self.assertEqual(self.pattern_class_builder.build.call_count, 1)
        self.assertEqual(self.pattern_class_resolver.resolve.call_count, 1)
        self.assertEqual(self.domain_update_extractor.extract.call_count, 1)
        self.assertEqual(self.norm_update_extractor.extract.call_count, 1)


if __name__ == '__main__':
    unittest.main()
