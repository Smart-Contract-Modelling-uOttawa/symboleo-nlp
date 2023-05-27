from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.selection.selected_node import SelectedNode

class IGetNodeChildren:
    def get(self, parent_node: InputUnit, contract: ISymboleoContract, prev_value: SelectedNode) -> List[InputUnit]:
        raise NotImplementedError()


class DefaultChildGetter(IGetNodeChildren):
    def get(self, parent_node: InputUnit, contract: ISymboleoContract, prev_value: SelectedNode) -> List[InputUnit]:
        return [x() for x in parent_node.children]