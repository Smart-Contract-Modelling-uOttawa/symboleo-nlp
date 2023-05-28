from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.elements.element import Element

from app.src.pattern_updaters.pattern_builder import IBuildPatterns
from app.src.update_processor.update_processor import IProcessUpdates

# Will likely need to specify the norm_component...
# Instead of key, can I use the ParmConfig...?
class ParameterOperation:
    def __init__(self, nl_key:str, parm_key:str, node_list: List[Element]):
        self.nl_key = nl_key
        self.parm_key = parm_key
        self.node_list = node_list # elements list


class IRefineParameter:
    def refine(self, contract: ISymboleoContract, op: ParameterOperation):
        raise NotImplementedError()


class ParameterRefiner(IRefineParameter):
    def __init__(
        self, 
        pattern_builder: IBuildPatterns,
        update_processor: IProcessUpdates
    ):
        self.__pattern_builder = pattern_builder
        self.__update_processor = update_processor


    def refine(self, contract: ISymboleoContract, op: ParameterOperation):
        # Get the norm
        norms = contract.get_norms_by_key(op.nl_key, op.parm_key)

        # Build pattern from node_list to get the NL text
        pattern = self.__pattern_builder.build(op.node_list)

        for norm in norms:
            # Extract all the required updates
            update_set = self.__update_processor.process(norm, pattern)

            # Run the Symboleo updates
            contract.run_updates(update_set)

        # Run the NL Update... Likely need the component here as well
        # Or maybe this goes outside of this. Either way, we need the input text
        contract.update_nl(op.nl_key, op.parm_key, 'TODO') #pattern.to_text()


        
        


        

