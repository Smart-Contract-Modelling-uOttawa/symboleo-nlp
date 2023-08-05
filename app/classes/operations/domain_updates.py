from typing import List
from app.classes.spec.declaration import Declaration
from app.classes.spec.domain_object import DomainObject

class DomainUpdates:
    def __init__(
        self,
        declarations: List[Declaration],
        domain_objects: List[DomainObject]
    ):
        self.declarations = declarations
        self.domain_objects = domain_objects