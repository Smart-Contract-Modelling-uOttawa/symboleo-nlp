import unittest
from unittest.mock import MagicMock

from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.domain_object import IDomainObject
from app.classes.spec.declaration import IDeclaration

from app.src.operations.domain_updater import DomainUpdater, DomainOperation

class DomainUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.sut = DomainUpdater()

    def test_domain_updater(self):
        contract = ISymboleoContract()
        contract.add_dm_object = MagicMock(return_value = None)
        contract.add_declaration = MagicMock(return_value = None)

        dobj = IDomainObject()
        decl = IDeclaration()
        op = DomainOperation(dobj, decl)     

        self.sut.update(contract, op)
        
        self.assertEqual(contract.add_dm_object.call_count, 1)
        self.assertEqual(contract.add_declaration.call_count, 1)


if __name__ == '__main__':
    unittest.main()