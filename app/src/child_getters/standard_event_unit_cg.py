from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.elements.element import Element

from app.classes.units.all_units import StandardEventUnit, ContractEventUnit, NormEventUnit, CommonEventUnit

from app.src.child_getters.child_getter import IGetUnitChildren

from app.classes.template_event.common_event_dict import COMMON_EVENT_DICT

class StandardEventUnitCG(IGetUnitChildren):
    def get(self, parent_unit: StandardEventUnit, contract: ISymboleoContract, element: Element) -> List[InputUnit]:
        contract_event_unit = ContractEventUnit()

        norm_event_unit = NormEventUnit(['obligation', 'power'])
    
        common_events = list(COMMON_EVENT_DICT.keys())
        common_event_unit = CommonEventUnit(common_events)

        return [contract_event_unit, norm_event_unit, common_event_unit]

