from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.norm import Norm
from app.classes.spec.predicate_function import PredicateFunction
from app.src.operations.refine_parameter.parm_configs import ParmOpCode
from app.classes.frames.frame import Frame

class RefinementOperation:
    def __init__(
        self,
        key: str,
        frame: Frame,
        contract: ISymboleoContract = None,
        norm: Norm = None,
        update_obj: any = None, #TODO: Specify this
        norm_component: str = None
    ):
        self.key = key
        self.frame = frame
        self.contract = contract
        self.norm = norm
        self.update_obj = update_obj
        self.norm_component = norm_component


class IRunRefinementOperation:
    def run(self, op: RefinementOperation):
        raise NotImplementedError()

class RefinementOperationRunner(IRunRefinementOperation):
    def run(self, op: RefinementOperation):
        frame = op.frame
        op_code = frame.op_code
        contract = op.contract
        norm = op.norm
        update_obj = op.update_obj
        norm_component = op.norm_component
        nl = frame.to_text()
        # This is where we may need the text component...

        # Perform the appropriate update
        # if op_code == ParmOpCode.ADD_DM_PROP:
        #     # TODO: I dont think this one will be needed. Events are added separately. Will likely remove
        #     # contract.add_dm_prop(update_obj, parm_config.obj_type, parm_config.obj_name)
        #     raise ValueError('Currently not supported.')
        
        if op_code == ParmOpCode.ADD_NORM:
            update_norm: Norm = update_obj
            contract.add_norm(update_norm, op.key, nl)
        
        elif op_code == ParmOpCode.ADD_TRIGGER:
            update_pred: PredicateFunction = update_obj
            contract.update_norm(norm, 'trigger', update_pred, op.key, nl)
        
        elif op_code == ParmOpCode.REFINE_PREDICATE:
            update_pred: PredicateFunction = update_obj
            contract.update_norm(norm, norm_component, update_pred, op.key, nl)
        
        else:
            raise NotImplementedError('Invalid operation requested')