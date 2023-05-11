class ParameterConfig:
    def __init__(self, norm_type: str, norm_id: str, norm_component: str = ''):
        self.norm_type = norm_type # obligations, powers 
        self.norm_id = norm_id # e.g. ob_delivery
        self.norm_component = norm_component # consequent, antecedent, trigger
