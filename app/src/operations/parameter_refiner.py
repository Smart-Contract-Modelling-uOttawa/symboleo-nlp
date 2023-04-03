from app.classes.symboleo_contract import SymboleoContract
from app.src.operations.parm_configs import ParameterConfig, ParmOpCode
from app.src.grammar.selection import Selection

from app.classes.grammar.selected_node import Basket
from app.src.grammar.selection import Selection
from app.src.frames.frame_checker import ICheckFrames

class ParameterOperation:
    def __init__(self, config: ParameterConfig, selection: Selection):
        self.config = config
        self.selection = selection

class IRefineParameter:
    def refine(self, contract: SymboleoContract, op: ParameterOperation):
        raise NotImplementedError()


class ParameterRefiner(IRefineParameter):
    def __init__(
            self, 
            frame_checker: ICheckFrames
        ):
        self.__frame_checker = frame_checker
    
    def refine(self, contract: SymboleoContract, op: ParameterOperation):
        selection = op.selection
        parm_config = op.config
        
        # Extract the frame
        frames = self.__frame_checker.check_all_frames(selection.nodes)
        frame = frames[0]
        frame_text = frame.to_text()
        print(f'\nNL: {frame_text}\n')

        # Convert to update_obj
        basket = Basket()

        try:
            norm = contract.get_norm(parm_config.norm_id, parm_config.norm_type)
            basket.initial_norm = norm
            basket.default_event = norm.get_default_event(parm_config.norm_component)
        except:
            norm = None

        update_obj = selection.to_obj(basket)
        op_code = frame.op_code

        # Perform the appropriate update
        if op_code == ParmOpCode.ADD_DM_PROP:
            contract.add_dm_prop(update_obj, parm_config.obj_type, parm_config.obj_name)
        
        elif op_code == ParmOpCode.ADD_NORM:
            contract.add_norm(update_obj)
        
        elif op_code == ParmOpCode.ADD_TRIGGER:
            # get the norm; Might just make 
            norm = contract.get_norm(parm_config.norm_id, parm_config.norm_type)
            norm.update('trigger', update_obj)
        
        elif op_code == ParmOpCode.REFINE_PREDICATE:
            norm = contract.get_norm(parm_config.norm_id, parm_config.norm_type)
            norm.update(parm_config.norm_component, update_obj)
        
        else:
            raise NotImplementedError('Invalid operation requested')
    

        