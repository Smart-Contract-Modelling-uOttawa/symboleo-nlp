from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.spec.norm import Norm
from app.src.operations.parm_configs import ParmOpCode

class RefinementOperation:
    def __init__(
        self,
        op_code: ParmOpCode,
        contract: ISymboleoContract = None,
        norm: Norm = None,
        update_obj: any = None, #TODO: Specify this
        norm_component: str = None
    ):
        self.op_code = op_code
        self.contract = contract
        self.norm = norm
        self.update_obj = update_obj
        self.norm_component = norm_component


class IRunRefinementOperation:
    def run(self, op: RefinementOperation):
        raise NotImplementedError()

class RefinementOperationRunner(IRunRefinementOperation):
    def run(self, op: RefinementOperation):
        op_code = op.op_code
        contract = op.contract
        norm = op.norm
        update_obj = op.update_obj
        norm_component = op.norm_component

        # Perform the appropriate update
        # if op_code == ParmOpCode.ADD_DM_PROP:
        #     # TODO: I dont think this one will be needed. Events are added separately. Will likely remove
        #     # contract.add_dm_prop(update_obj, parm_config.obj_type, parm_config.obj_name)
        #     raise ValueError('Currently not supported.')
        
        if op_code == ParmOpCode.ADD_NORM:
            contract.add_norm(update_obj)
        
        elif op_code == ParmOpCode.ADD_TRIGGER:
            norm.update('trigger', update_obj)
        
        elif op_code == ParmOpCode.REFINE_PREDICATE:
            norm.update(norm_component, update_obj)
        
        else:
            raise NotImplementedError('Invalid operation requested')