from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.selection.selected_node import SelectedNode

from app.src.frames.frame_checker import ICheckFrames
from app.src.operations.refine_parameter2.update_extractor import IExtractUpdates

# Will likely need to specify the norm_component...
class ParameterOperation:
    def __init__(self, key:str, node_list: List[SelectedNode]):
        self.key = key
        self.node_list = node_list


class IRefineParameter:
    def refine(self, contract: ISymboleoContract, op: ParameterOperation):
        raise NotImplementedError()


class ParameterRefiner(IRefineParameter):
    def __init__(
        self, 
        frame_checker: ICheckFrames,
        update_extractor: IExtractUpdates
    ):
        self.__frame_checker = frame_checker
        self.__update_extractor = update_extractor


    def refine(self, contract: ISymboleoContract, op: ParameterOperation):
        # Get the norm.. Make a convenience function on the contract for this
        norm = contract.get_norm_by_key(op.key)

        # Build frame from node_list to get the NL text
        frame = self.__frame_checker.get_frame(op.node_list)

        # Extract all the required updates
        ## Will include declarations, dmos, norms, etc
        update_set = self.__update_extractor.extract(norm, op.node_list)

        # Run the update set against the contract
        contract.run_updates(update_set)

        # Update the NL... Likely need the component here as well
        contract.update_nl(op.key, frame.to_text())


        
        


        

