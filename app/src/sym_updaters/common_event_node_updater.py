from typing import Dict
from app.classes.spec.norm import INorm
from app.classes.spec.sym_event import VariableEvent
from app.classes.elements.element import Element
from app.classes.elements.standard_event_elements import CommonEventNode
from app.classes.operations.contract_update_obj import ContractUpdateObj
from app.classes.operations.update_package import UpdatePackage
from app.src.sym_updaters.package_updater import IUpdatePackage

from app.classes.template_event.common_event import CommonEvent
from app.src.sym_updaters.common_event.i_map_common_events import IMapCommonEvents
from app.src.sym_updaters.custom_event.domain_model_mapper import IMapDeclarationToDomain


class CommonEventNodeUpdater(IUpdatePackage):
    def __init__(
        self, 
        mapper_dict: Dict[str, IMapCommonEvents],
        domain_mapper: IMapDeclarationToDomain
    ):
        self.__mapper_dict = mapper_dict
        self.__domain_mapper = domain_mapper
    
    # Interesting. We are getting it twice... May not actually need the value to be Common Event anymore.
    ## Could be a custom event. Since we get the key..
    ## Takes the load off the FinalNode...
    def update_package(self, norm: INorm, node: CommonEventNode,  value: CommonEvent) -> UpdatePackage:
        mapper = self.__mapper_dict[value.common_event_key]
        declaration = mapper.map(value)
        domain_obj = self.__domain_mapper.map(declaration)

        update_obj = ContractUpdateObj(
            domain_objects=[domain_obj],
            declarations=[declaration]
        )
        new_value = VariableEvent(declaration.name)

        return UpdatePackage(update_obj, new_value)
