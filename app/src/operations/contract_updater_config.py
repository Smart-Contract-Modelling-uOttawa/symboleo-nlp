from enum import Enum

from app.src.operations.parm_configs import ParameterConfig
from app.src.grammar.selection import Selection

from app.classes.spec.domain_model import DomainObject
from app.classes.spec.declaration import Declaration

class OpCode(Enum):
    UPDATE_PARM = 1
    ADD_TERMINATION_POWER = 2
    ADD_DOMAIN_OBJECT = 3


class UpdateConfig:
    def __init__(
            self, 
            op_code: OpCode, 

            # Parm update
            selection: Selection = None, 
            parm_config: ParameterConfig = None,
            
            # DM Update
            dm_obj_type: str = '',
            domain_object: DomainObject = None,
            declaration: Declaration = None,

            # Termination
            norm_id: str = '',
            debtor: str = '',
            creditor: str = ''
        ):
        self.op_code = op_code
        self.selection: Selection = selection
        self.parm_config: ParameterConfig = parm_config
        
        self.dm_obj_type = dm_obj_type
        self.domain_object = domain_object
        self.declaration = declaration

        self.norm_id = norm_id
        self.debtor = debtor
        self.creditor = creditor
