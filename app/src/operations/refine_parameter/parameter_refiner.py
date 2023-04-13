from app.classes.spec.symboleo_contract import SymboleoContract

from app.src.operations.refine_parameter.parm_configs import ParameterConfig, ParmOpCode
from app.src.grammar.selection import ISelection

from app.classes.selection.selected_node import Basket
from app.src.frames.frame_checker import ICheckFrames
from app.src.operations.refine_parameter.operation_runner import IRunRefinementOperation, RefinementOperation

# TODO: May not need both the config and the key... the key should give you everything about the config (I think)
class ParameterOperation:
    def __init__(self, config: ParameterConfig, selection: ISelection, key: str):
        self.config = config
        self.selection = selection
        self.key = key

class IRefineParameter:
    def refine(self, contract: SymboleoContract, op: ParameterOperation):
        raise NotImplementedError()

# TODO: Will need to clean up, break out, and test this one
class ParameterRefiner(IRefineParameter):
    def __init__(
            self, 
            frame_checker: ICheckFrames,
            runner: IRunRefinementOperation
        ):
        self.__frame_checker = frame_checker
        self.__runner = runner
        self.__component_dict = {
            ParmOpCode.REFINE_PREDICATE: 'consequent',
            ParmOpCode.ADD_TRIGGER: 'trigger'
            # Will eventually need the ADD_NORM here...
        }
    
    def refine(self, contract: SymboleoContract, op: ParameterOperation):
        selection = op.selection
        parm_config = op.config
        
        # Extract the frame
        node_list = selection.get_nodes()
        frame = self.__frame_checker.check_all_frames(node_list)[0]
        op_code = frame.op_code
        
        basket = Basket()
        norm_component = None

        try:
            norm = contract.get_norm(parm_config.norm_id, parm_config.norm_type)
            basket.initial_norm = norm
            norm_component = self.__component_dict[op_code]
            basket.default_event = norm.get_default_event(norm_component)
        except:
            norm = None

        update_obj = selection.to_obj(basket)
        
        self.__runner.run(RefinementOperation(
            op.key,
            frame,
            contract,
            norm,
            update_obj,
            norm_component
        ))


