from app.src.sym_updaters.custom_event.custom_event_node_updater import CustomEventNodeUpdater
from app.src.sym_updaters.custom_event.asset_type_extractor import AssetTypeExtractor
from app.src.sym_updaters.custom_event.asset_decl_extractor import AssetDeclarationExtractor
from app.src.sym_updaters.custom_event.asset_declaration_mapper import AssetDeclarationMapper
from app.src.sym_updaters.custom_event.declaration_prop_mapper import DeclarationPropMapper
from app.src.sym_updaters.custom_event.event_declaration_mapper import EventDeclarationMapper
from app.src.sym_updaters.custom_event.domain_model_mapper import DeclarationToDomainMapper

class CustomEventNodeUpdaterBuilder:
    @staticmethod
    def build() -> CustomEventNodeUpdater:
        
        asset_type_extractor = AssetTypeExtractor()
        asset_extractor = AssetDeclarationExtractor(asset_type_extractor)
        asset_decl_mapper = AssetDeclarationMapper(asset_extractor) 

        prop_mapper = DeclarationPropMapper(asset_type_extractor)
        event_decl_mapper = EventDeclarationMapper(prop_mapper)

        domain_mapper = DeclarationToDomainMapper()

        return CustomEventNodeUpdater(
            asset_decl_mapper,
            event_decl_mapper,
            domain_mapper
        )
