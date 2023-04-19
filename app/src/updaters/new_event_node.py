from app.classes.spec.norm import INorm
from app.classes.spec.sym_event import VariableEvent
from app.classes.selection.selected_node import SelectedNode
from app.classes.other.contract_update_obj import UpdatePackage, ContractUpdateObj
from app.src.updaters.iupdate_package import IUpdatePackage
from app.classes.other.frame_event import FrameEvent
from app.src.nlp.frame_event_mappers import IMapEventToDeclaration, IMapEventToDomain

class NewEventNodeUpdater(IUpdatePackage):
    def __init__(
        self,
        decl_mapper: IMapEventToDeclaration,
        domain_mapper: IMapEventToDomain
    ):
        self.__decl_mapper = decl_mapper
        self.__domain_mapper = domain_mapper


    # I could also set up the possibility for the node value itself...
    def update_package(self, norm: INorm, node: SelectedNode,  value: any) -> UpdatePackage:
        if type(value) == FrameEvent:
            dmo = self.__domain_mapper.map(value)
            decl = self.__decl_mapper.map(value, dmo)

            evt_name = f'evt_{value.get_event_name()}'
            new_value = VariableEvent(evt_name)

            return UpdatePackage(ContractUpdateObj(domain_objects=[dmo], declarations=[decl]), new_value = new_value)
        

