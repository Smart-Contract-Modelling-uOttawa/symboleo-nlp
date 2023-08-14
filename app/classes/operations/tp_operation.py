from app.classes.spec.norm_config import NormConfig

class TPOperation:
    def __init__(self, norm_id:str, norm_config: NormConfig, debtor: str, creditor: str):
        self.norm_id = norm_id
        self.norm_config = norm_config
        self.debtor = debtor
        self.creditor = creditor