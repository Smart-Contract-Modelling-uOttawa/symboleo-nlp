class TestUnit:
    def __init__(
        self, 
        norm_type: str, 
        id: str, 
        str_component: str, 
        customization: str, 
        expected_sym: str
    ):
        self.norm_type = norm_type #obligations, suriving_obligations, powers
        self.id = id
        self.str_component = str_component #trigger, antecedent, consequent
        self.customization = customization
        self.expected_sym = expected_sym