from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.selection.selected_node import SelectedNode

from app.classes.units.all_nodes import BeforeNode, EventNode, DateNode, TimepointNode
from app.src.child_getters.child_getter import IGetNodeChildren

from app.src.child_getters.domain_timepoint_extractor import IExtractDomainTimePoints

class BeforeNodeCG(IGetNodeChildren):
    def __init__(self, domain_timepoint_extractor: IExtractDomainTimePoints):
        self.__domain_timepoint_extractor = domain_timepoint_extractor

    def get(self, parent_node: BeforeNode, contract: SymboleoContract, prev_value: SelectedNode) -> List[InputUnit]:
        children: List[InputUnit] = []

        children.append(EventNode())
        children.append(DateNode())

        domain_timepoints = self.__domain_timepoint_extractor.extract(contract)
        dtp_node = TimepointNode(domain_timepoints)
        children.append(dtp_node)
        
        return children

