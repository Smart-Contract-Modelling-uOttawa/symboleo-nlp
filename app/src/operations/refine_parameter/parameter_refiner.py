from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.selection.selected_node import SelectedNode

from app.src.frame_updaters.frame_builder import IBuildFrames
from app.src.sym_updaters.update_extractor import IExtractUpdates

# Will likely need to specify the norm_component...
# Instead of key, can I use the ParmConfig...?
class ParameterOperation:
    def __init__(self, nl_key:str, parm_key:str, node_list: List[SelectedNode]):
        self.nl_key = nl_key
        self.parm_key = parm_key
        self.node_list = node_list


class IRefineParameter:
    def refine(self, contract: ISymboleoContract, op: ParameterOperation):
        raise NotImplementedError()


class ParameterRefiner(IRefineParameter):
    def __init__(
        self, 
        frame_builder: IBuildFrames,
        update_extractor: IExtractUpdates
    ):
        self.__frame_builder = frame_builder
        self.__update_extractor = update_extractor


    def refine(self, contract: ISymboleoContract, op: ParameterOperation):
        # Get the norm
        norms = contract.get_norms_by_key(op.nl_key, op.parm_key)

        # Build frame from node_list to get the NL text
        frame = self.__frame_builder.build(op.node_list)


        for norm in norms:
            # Extract all the required updates
            update_set = self.__update_extractor.extract(norm, op.node_list)

            # Run the Symboleo updates
            contract.run_updates(update_set)

        # Run the NL Update... Likely need the component here as well
        contract.update_nl(op.nl_key, op.parm_key, frame.to_text())


        
        


        

