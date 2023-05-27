from typing import List
from app.classes.frames.frame import Frame
from app.classes.selection.selected_node import SelectedNode
from app.classes.spec.norm import Norm
from app.classes.operations.contract_update_obj import ContractUpdateObj

from app.src.update_processor.pattern_handlers.handle_object import HandleObject
from app.src.update_processor.domain_update_extractor import IExtractDomainUpdates
from app.src.update_processor.norm_update_extractor import IExtractNormUpdates

class IProcessUpdates:
    def process(self, norm: Norm, frame: Frame):
        raise NotImplementedError()


class UpdateProcessor(IProcessUpdates):
    def __init__(
        self,
        domain_update_extractor: IExtractDomainUpdates,
        norm_update_extractor: IExtractNormUpdates
    ):
        self.__domain_update_extractor = domain_update_extractor
        self.__norm_update_extractor = norm_update_extractor

    
    def process(self, norm: Norm, frame: Frame) -> ContractUpdateObj:
        # Extract domain and declaration updates
        domain_updates = self.__domain_update_extractor.extract(frame)

        # Interesting... We could run these updates on the contract first...
        # Maybe not though. 
        # The problem is that we want the event
        
        # Build the handle_object -> complex..

        # Extract norms
        handle_object = HandleObject(norm)

        # This will require a bundle of arguments: Norm, contract, domain_objects, declarations, etc. 
        norms = self.__norm_update_extractor.extract(frame, handle_object)

        update_obj = ContractUpdateObj(norms, domain_updates.domain_objects, domain_updates.declarations)

        return update_obj