from app.classes.spec.norm import INorm
from app.classes.spec.sym_event import VariableEvent
from app.classes.selection.selected_node import SelectedNode
from app.classes.operations.update_package import UpdatePackage
from app.classes.operations.contract_update_obj import ContractUpdateObj
from app.classes.custom_event.custom_event import CustomEvent

from app.src.sym_updaters.package_updater import IUpdatePackage
from app.src.sym_updaters.custom_event.event_declaration_mapper import IMapEventToDeclaration
from app.src.sym_updaters.custom_event.asset_declaration_mapper import IMapAssetDeclarations
from app.src.sym_updaters.custom_event.domain_model_mapper import IMapDeclarationToDomain

class CustomEventNodeUpdater(IUpdatePackage):
    def __init__(
        self,
        asset_decl_mapper: IMapAssetDeclarations,
        event_decl_mapper: IMapEventToDeclaration,
        domain_mapper: IMapDeclarationToDomain
    ):
        self.__asset_decl_mapper = asset_decl_mapper
        self.__event_decl_mapper = event_decl_mapper
        self.__domain_mapper = domain_mapper


    def update_package(self, norm: INorm, node: SelectedNode,  value: any) -> UpdatePackage:
        if type(value) == CustomEvent:
            # May need to pass in existing declarations from the contract
            decls = self.__asset_decl_mapper.map(value)

            # Might then be passing asset_decls into this
            # Any Noun phrase should be an asset by this point... I think...
            event_decl = self.__event_decl_mapper.map(value)
            
            decls.append(event_decl)
            dmos = [self.__domain_mapper.map(x) for x in decls]

            new_value = VariableEvent(event_decl.name)
            
            update_obj = ContractUpdateObj(
                domain_objects=dmos,
                declarations=decls
            )

            return UpdatePackage(update_obj, new_value)
        

