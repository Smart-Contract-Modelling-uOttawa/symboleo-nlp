from typing import List
from app.classes.spec.declaration import Declaration
from app.classes.spec.domain_object import DomainObject
from app.classes.spec.contract_spec_parameter import ContractSpecParameter

class DomainUpdates:
    def __init__(
        self,
        declarations: List[Declaration],
        domain_objects: List[DomainObject],
        contract_parms: List[ContractSpecParameter]
    ):
        self.declarations = declarations
        self.domain_objects = domain_objects
        self.contract_parms = contract_parms