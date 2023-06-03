from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.operations.parameter_operation import ParameterOperation

from app.src.pattern_builder.pattern_builder import IBuildPatterns
from app.src.update_processor.update_processor import IProcessUpdates

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

        # Build pattern from elements to get the NL text
        pattern = self.__pattern_builder.build(op.elements)

        for norm in norms:
            # Extract all the required updates
            update_set = self.__update_processor.process(norm, pattern, contract)

            # Run the Symboleo updates
            contract.run_updates(update_set)

        # Extract the NL and update the contract
        #nl_update = self.__nl_extractor.extract(op.elements)
        nl_update = pattern.to_text()
        contract.update_nl(op.nl_key, op.parm_key, nl_update)


        
        


        


