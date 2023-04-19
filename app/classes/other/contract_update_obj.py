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
    

    def print_me(self):
        print(f'-Norms: {len(self.norms)}')
        print(f'-Decls: {len(self.declarations)}')
        print(f'-DMOs: {len(self.domain_objects)}')


    def merge(self, other: ContractUpdateObj):
        if not other:
            return

        for n in (other.norms or []):
            #next_norm = copy.deepcopy(n)
            self.norms.append(n)
        
        for d in (other.declarations or []):
            #next_d = copy.deepcopy(d)
            self.declarations.append(d)
        
        for dm in (other.domain_objects or []):
           # next_dmo = copy.deepcopy(dm)
            self.domain_objects.append(dm)



# TODO: Want to strongly type the child_obj... but probably cant.
class UpdatePackage:
    def __init__(self, update_obj: ContractUpdateObj = None, new_value: any = None):
        self.update_obj = update_obj
        self.new_value = new_value
