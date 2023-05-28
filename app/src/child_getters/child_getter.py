from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.elements.element import Element

class IGetNodeChildren:
    def get(self, parent_node: InputUnit, contract: ISymboleoContract, prev_value: Element) -> List[InputUnit]:
        raise NotImplementedError()


class DefaultChildGetter(IGetNodeChildren):
    def get(self, parent_node: InputUnit, contract: ISymboleoContract, prev_value: Element) -> List[InputUnit]:
        return [x() for x in parent_node.children]