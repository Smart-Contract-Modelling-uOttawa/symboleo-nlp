from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.selection.selected_node import SelectedNode

class IGetNodeChildren:
    def get(self, parent_node: AbstractNode, contract: ISymboleoContract, prev_value: SelectedNode) -> List[AbstractNode]:
        raise NotImplementedError()


class DefaultChildGetter(IGetNodeChildren):
    def get(self, parent_node: AbstractNode, contract: ISymboleoContract, prev_value: SelectedNode) -> List[AbstractNode]:
        return [x() for x in parent_node.children]