from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.elements.element import Element

from app.classes.units.all_units import BeforeUnit, EventUnit, DateUnit, TimepointUnit
from app.src.selection.child_getters.child_getter import IGetUnitChildren

from app.src.selection.child_getters.domain_timepoint_extractor import IExtractDomainTimePoints

class BeforeUnitCG(IGetUnitChildren):
    def __init__(self, domain_timepoint_extractor: IExtractDomainTimePoints):
        self.__domain_timepoint_extractor = domain_timepoint_extractor

    def get(self, parent_unit: BeforeUnit, contract: SymboleoContract) -> List[InputUnit]:
        children: List[InputUnit] = []

        children.append(EventUnit())
        children.append(DateUnit())

        domain_timepoints = self.__domain_timepoint_extractor.extract(contract)
        dtp_unit = TimepointUnit(domain_timepoints)
        children.append(dtp_unit)
        
        return children

