from typing import List
from app.classes.operations.op_code import OpCode
from app.classes.spec.domain_object import DomainObject
from app.classes.spec.declaration import Declaration
from app.classes.operations.user_input import UserInput

class UpdateConfig:
    def __init__(
            self, 
            op_code: OpCode = None, 

            # Parm update
            user_inputs: List[UserInput] = None,
            #selection: Selection = None, 
            #parm_config: ParameterConfig = None,
            nl_key: str = None,
            parm_key: str = None,
            
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
        self.user_inputs = user_inputs
        #self.selection = selection
        #self.parm_config: ParameterConfig = parm_config
        self.nl_key = nl_key
        self.parm_key = parm_key
        
        self.dm_obj_type = dm_obj_type
        self.domain_object = domain_object
        self.declaration = declaration

        self.norm_id = norm_id
        self.debtor = debtor
        self.creditor = creditor

