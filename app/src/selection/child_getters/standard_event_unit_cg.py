from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.elements.element import Element

from app.classes.units.all_units import StandardEventUnit, ContractEventUnit, NormEventUnit, CommonEventUnit

from app.src.selection.child_getters.child_getter import IGetUnitChildren

class StandardEventUnitCG(IGetUnitChildren):
    def get(self, parent_unit: StandardEventUnit, contract: ISymboleoContract) -> List[InputUnit]:
        contract_event_unit = ContractEventUnit()

        norm_event_unit = NormEventUnit(['obligation', 'power'])
    

        return [contract_event_unit, norm_event_unit]

