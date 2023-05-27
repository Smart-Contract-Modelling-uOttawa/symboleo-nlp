import unittest
from unittest.mock import MagicMock
from app.classes.spec.declaration import Declaration, DeclarationProp

from tests.helpers.test_contract import get_test_contract

class AddDeclarationTests(unittest.TestCase):
    def test_add_declaration(self):
        contract = get_test_contract()
        new_name1 = 'abc_xyz'
        new_name2 = 'xyz_abc'
        new_value = 'some_value'
        decl1 = Declaration(new_name1, 'events', 'Action', [ DeclarationProp('k', new_value, 'String')])
        decl2 = Declaration(new_name2, 'events', 'Action', [ DeclarationProp('k', new_value, 'String')])

        contract.add_declaration(decl1)
        contract.add_declaration(decl2)

        decls = contract.contract_spec.declarations

        found_decl1: Declaration = decls[new_name1]
        found_decl2: Declaration = decls[new_name2]
        self.assertEqual(found_decl1.name, new_name1)
        self.assertEqual(found_decl2.name, new_name2)

        parms = contract.contract_spec.parameters
        # TODO: Will need to re-add parms when I figure it out
        found_parms = [x for x in parms if x.name == new_value]
        #self.assertEqual(len(found_parms), 1)

        #self.assertEqual(found_parms[0].type, 'String')
    
  
if __name__ == '__main__':
    unittest.main()