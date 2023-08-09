from __future__ import annotations
from typing import List

from app.classes.spec.norm import INorm
from app.classes.spec.domain_object import IDomainObject
from app.classes.spec.declaration import IDeclaration
from app.classes.spec.contract_spec_parameter import ContractSpecParameter

class ContractUpdateObj:
    def __init__(
        self,
        norms: List[INorm] = None,
        domain_objects: List[IDomainObject] = None,
        declarations: List[IDeclaration] = None,
        contract_parms: List[ContractSpecParameter] = None,
        nl_update: str = None
    ):
        self.norms = norms or []
        self.domain_objects = domain_objects or []
        self.declarations = declarations or []
        self.contract_parms = contract_parms or []
        self.nl_update = nl_update
    