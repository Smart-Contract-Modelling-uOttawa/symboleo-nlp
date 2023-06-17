import unittest
from app.classes.spec.symboleo_contract import SymboleoContract
from app.templates.template_getter import get_template
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder

from app.src.selection.child_getters.child_getter_dict import ChildGetterDictConstructor
from app.src.selection.child_node_getter import ChildNodeGetter
from app.src.selection.element_list_selector_builder import ElementListSelector

from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType
from app.classes.units.all_units import *

from tests.helpers.test_contract import get_test_contract


class TreeGen:
    def generate_init(self):
        child_getter_dict = ChildGetterDictConstructor.build()
        self.sut = ChildNodeGetter(child_getter_dict)
        self.contract = get_test_contract()

        self._generate(RootUnit())

    

    def _generate(self, node: InputUnit, current_path=''):
    
        current_path += node.unit_type.name + ' '

        children = node.children

        if len(children) == 0:
            self._process(current_path)
        elif len(children) == 1 and children[0].unit_type == UnitType.FINAL_NODE:
            self._process(current_path)
        else:
            for c in children:
                self._generate(c, current_path)


    def _process(self, path):
        print('\n\n-->', path)

class FullCNLGenerationTests(unittest.TestCase):
    def setUp(self) -> None:
        #child_getter_dict = ChildGetterDictConstructor.build()
        #self.sut = ChildNodeGetter(child_getter_dict)
        # dont need to test the element list selector
        # just need to test the tree...
        self.s = 0

    def test_cnl_generation(self):
        tree_gen = TreeGen()

        tree_gen.generate_init()



if __name__ == '__main__':
    unittest.main()