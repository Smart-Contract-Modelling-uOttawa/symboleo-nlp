import copy
from typing import List
from app.classes.symboleo_contract import DomainModel
from app.classes.spec.domain_model import DomainObject

class TemplateHelpers:

    @staticmethod
    def create_declaration(dm: DomainModel, obj_type: str, obj_name: str, obj_key: str, props:List = []):
        dm_obj: DomainObject = copy.deepcopy(dm.__dict__[obj_type][obj_name])
        dm_obj.name = obj_key
        for k,v in props:
            dm_obj.set_prop(k, v)
        return dm_obj