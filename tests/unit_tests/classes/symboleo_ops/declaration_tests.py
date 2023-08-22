import unittest
from unittest.mock import MagicMock

from app.classes.spec.declaration import DeclarationProp, EventDeclaration, RoleDeclaration
from app.classes.spec.sym_event import VariableEvent

class DeclarationTests(unittest.TestCase):
    def test_evt_declaration(self):
        test_decl = EventDeclaration('evt_test', 'Test', [
            DeclarationProp('test_prop', 'X', 'String')
        ])
        
        res = test_decl.to_obj()

        self.assertEqual(res, VariableEvent('evt_test'))

    def test_role_declaration(self):
        test_decl = RoleDeclaration('name', 'Buyer', id='name_id')

        res = test_decl.to_obj()
        self.assertEqual(res, 'name_id')
    
  
if __name__ == '__main__':
    unittest.main()