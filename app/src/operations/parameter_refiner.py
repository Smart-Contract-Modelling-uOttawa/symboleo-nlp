from app.classes.spec.symboleo_contract import SymboleoContract
from app.src.operations.parm_configs import ParameterConfig, ParmOpCode
from app.src.grammar.selection import Selection

from app.classes.selection.selected_node import Basket
from app.src.grammar.selection import Selection
from app.src.frames.frame_checker import ICheckFrames

# TODO: Might be able to get rid of the parameterconfig...
class ParameterOperation:
    def __init__(self, config: ParameterConfig, selection: Selection):
        self.config = config
        self.selection = selection

class IRefineParameter:
    def refine(self, contract: SymboleoContract, op: ParameterOperation):
        raise NotImplementedError()

# TODO: Will need to clean up, break out, and test this one
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
        op_code = frame.op_code
        print(f'\nNL: {frame_text}\n')

        # Convert to update_obj
        basket = Basket()

        try:
            # TODO: Should just be passing the norm right in
            norm = contract.get_norm(parm_config.norm_id, parm_config.norm_type)
            basket.initial_norm = norm
            norm_component = self._get_component(op_code)
            # If I have the norm, then I may not need the default event either. Leave it for now though
            basket.default_event = norm.get_default_event(norm_component)
        except:
            norm = None

        update_obj = selection.to_obj(basket)
        

        # Perform the appropriate update
        if op_code == ParmOpCode.ADD_DM_PROP:
            # TODO: I dont think this one will be needed. Events are added separately
            contract.add_dm_prop(update_obj, parm_config.obj_type, parm_config.obj_name)
        
        elif op_code == ParmOpCode.ADD_NORM:
            contract.add_norm(update_obj)
        
        elif op_code == ParmOpCode.ADD_TRIGGER:
            # get the norm; Might just make 
            norm = contract.get_norm(parm_config.norm_id, parm_config.norm_type)
            norm.update('trigger', update_obj)
        
        elif op_code == ParmOpCode.REFINE_PREDICATE:
            norm = contract.get_norm(parm_config.norm_id, parm_config.norm_type)
            norm.update(norm_component, update_obj)
        
        else:
            raise NotImplementedError('Invalid operation requested')
    
    
    # Will probably split out separately...
    def _get_component(self, op_code: ParmOpCode):
        if op_code == ParmOpCode.REFINE_PREDICATE:
            return 'consequent'
        
        if op_code == ParmOpCode.ADD_TRIGGER:
            return 'trigger'
        
        raise ValueError('Invalid op code')
        