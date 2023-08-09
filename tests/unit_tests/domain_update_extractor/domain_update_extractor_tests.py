import unittest
from unittest.mock import MagicMock
from app.classes.spec.declaration import Declaration, EventDeclaration
from app.classes.spec.domain_object import DomainObject
from app.classes.spec.contract_spec_parameter import ContractSpecParameter

from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternClass
from app.src.domain_update_extractor.domain_update_extractor import DomainUpdateExtractor
from app.src.domain_update_extractor.asset_declaration_mapper import IMapAssetDeclarations
from app.src.domain_update_extractor.declaration_mapper import IMapDeclarations
from app.src.domain_update_extractor.domain_model_mapper import IMapDeclarationToDomain
from app.src.domain_update_extractor.contract_parm_mapper import IMapContractParms

from tests.helpers.test_objects import CustomEvents

class DomainUpdateExtractorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.decl_mapper = IMapDeclarations()
        self.domain_mapper = IMapDeclarationToDomain()
        self.csp_mapper = IMapContractParms()

        self.sut = DomainUpdateExtractor(
            self.decl_mapper,
            self.domain_mapper,
            self.csp_mapper
        )

    def test_domain_update_extractor(self):
        asset_decls = [
            Declaration('a1', 'A1', 'assets', []),
            Declaration('a2', 'A2', 'assets', []),
            EventDeclaration('evt_e1', 'E1', 'events', [])
        ]
        self.decl_mapper.map = MagicMock(return_value=asset_decls)

        domain_obj = DomainObject('a', 'b', [])
        self.domain_mapper.map = MagicMock(return_value=domain_obj)

        csps = [ContractSpecParameter('a','b')]
        self.csp_mapper.map = MagicMock(return_value = csps)

        pattern_class = EventPatternClass()
        pattern_class.nl_event = CustomEvents.paying()

        result = self.sut.extract(pattern_class, None, None)

        self.assertEqual(len(result.declarations), 3)
        self.assertEqual(len(result.domain_objects), 3)
        self.assertEqual(len(result.contract_parms), 1)
        self.assertEqual(result.declarations[2].name, 'evt_e1')
        self.assertEqual(self.decl_mapper.map.call_count, 1)
        self.assertEqual(self.domain_mapper.map.call_count, 3)
        self.assertEqual(self.csp_mapper.map.call_count, 1)

    
    def test_domain_update_extractor_empty(self):
        self.decl_mapper.map = MagicMock(return_value=[])
        self.domain_mapper.map = MagicMock(return_value=None)
        self.csp_mapper.map = MagicMock(return_value=[])

        pattern_class = PatternClass()
        result = self.sut.extract(pattern_class, None, None)

        self.assertEqual(len(result.declarations), 0)
        self.assertEqual(len(result.domain_objects), 0)
        self.assertEqual(len(result.contract_parms), 0)
        self.assertEqual(self.decl_mapper.map.call_count, 1)
        self.assertEqual(self.domain_mapper.map.call_count, 0)
        self.assertEqual(self.csp_mapper.map.call_count, 1)


if __name__ == '__main__':
    unittest.main()