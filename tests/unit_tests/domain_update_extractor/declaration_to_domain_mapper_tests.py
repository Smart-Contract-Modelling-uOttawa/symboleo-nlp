import unittest
from unittest.mock import MagicMock

from app.classes.spec.declaration import DeclarationProp, EventDeclaration, AssetDeclaration
from app.classes.spec.domain_object import Asset, DomainEvent, DomainProp
from app.src.domain_update_extractor.domain_model_mapper import DeclarationToDomainMapper

class DeclarationToDomainMapperTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = DeclarationToDomainMapper()

    def test_declaration_to_domain_mapper_event(self):
        evt = EventDeclaration('test', 'Test', [
            DeclarationProp('k', 'v', 't')
        ])
        expected_event = DomainEvent('Test', [DomainProp('k','t')])
        result = self.sut.map(evt)
        self.assertEqual(result, expected_event)
    
    def test_declaration_to_domain_mapper_asset(self):
        evt = AssetDeclaration('test', 'Test', [
            DeclarationProp('k', 'v', 't')
        ])
        expected = Asset('Test', [DomainProp('k','t')])
        result = self.sut.map(evt)
        self.assertEqual(result, expected)
    
if __name__ == '__main__':
    unittest.main()