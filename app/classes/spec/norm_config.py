from app.classes.spec.norm import INorm
from app.classes.spec.parameter_config import ParameterConfig

class NormConfig:
    def __init__(self, norm: INorm, parm_config: ParameterConfig):
        self.norm = norm
        self.parm_config = parm_config