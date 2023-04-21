from app.classes.spec.norm import INorm
from app.classes.spec.sym_event import VariableEvent
from app.classes.selection.selected_node import SelectedNode
from app.classes.other.contract_update_obj import UpdatePackage, ContractUpdateObj
from app.src.updaters.iupdate_package import IUpdatePackage
from app.classes.other.frame_event import FrameEvent
from app.src.nlp.frame_event.event_declaration_mapper import IMapEventToDeclaration
from app.src.nlp.frame_event.asset_declaration_mapper import IMapAssetDeclarations
from app.src.nlp.frame_event.domain_model_mapper import IMapDeclarationToDomain

class NewEventNodeUpdater(IUpdatePackage):
    def __init__(
        self,
        asset_decl_mapper: IMapAssetDeclarations,
        event_decl_mapper: IMapEventToDeclaration,
        domain_mapper: IMapDeclarationToDomain
    ):
        self.__asset_decl_mapper = asset_decl_mapper
        self.__event_decl_mapper = event_decl_mapper
        self.__domain_mapper = domain_mapper


    # I could also set up the possibility for the node value itself...
    def update_package(self, norm: INorm, node: SelectedNode,  value: any) -> UpdatePackage:
        if type(value) == FrameEvent:
            
            # Need to pass in existing declarations from the contract
            decls = self.__asset_decl_mapper.map(value)

            # Will then be passing asset_decls into this
            event_decl = self.__event_decl_mapper.map(value) # Any Noun phrase must be an asset by this point... so prob dont need the is_asset anymore
            
            decls.append(event_decl)
            dmos = [self.__domain_mapper.map(x) for x in decls]

            new_value = VariableEvent(event_decl.name)
            
            update_obj = ContractUpdateObj(
                domain_objects=dmos,
                declarations=decls
            )

            return UpdatePackage(update_obj, new_value)
        

