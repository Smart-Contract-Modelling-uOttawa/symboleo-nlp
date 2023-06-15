from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.elements.element import Element

class IGetUnitChildren:
    def get(self, parent_unit: InputUnit, contract: ISymboleoContract) -> List[InputUnit]:
        raise NotImplementedError()


class DefaultChildGetter(IGetUnitChildren):
    def get(self, parent_unit: InputUnit, contract: ISymboleoContract) -> List[InputUnit]:
        return [x() for x in parent_unit.children]