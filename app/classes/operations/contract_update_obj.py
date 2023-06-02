from __future__ import annotations
from typing import List

from app.classes.spec.norm import INorm
from app.classes.spec.domain_object import IDomainObject
from app.classes.spec.declaration import IDeclaration

class ContractUpdateObj:
    def __init__(
        self,
        norms: List[INorm] = None,
        domain_objects: List[IDomainObject] = None,
        declarations: List[IDeclaration] = None
    ):
        self.norms = norms or []
        self.domain_objects = domain_objects or []
        self.declarations = declarations or []
    
    
    def merge(self, other: ContractUpdateObj):
        if not other:
            return
        
        for n in (other.norms or []):
            self.norms.append(n)
        
        for d in (other.declarations or []):
            self.declarations.append(d)
        
        for dm in (other.domain_objects or []):
            self.domain_objects.append(dm)

