from app.src.updaters.new_event_node import NewEventNodeUpdater

from app.src.nlp.frame_event.asset_type_extractor import AssetTypeExtractor
from app.src.nlp.frame_event.asset_decl_extractor import AssetDeclarationExtractor
from app.src.nlp.frame_event.asset_declaration_mapper import AssetDeclarationMapper
from app.src.nlp.frame_event.declaration_prop_mapper import DeclarationPropMapper
from app.src.nlp.frame_event.event_declaration_mapper import EventDeclarationMapper
from app.src.nlp.frame_event.domain_model_mapper import DeclarationToDomainMapper

class NewEventNodeUpdaterBuilder:
    @staticmethod
    def build() -> NewEventNodeUpdater:
        
        asset_type_extractor = AssetTypeExtractor()
        asset_extractor = AssetDeclarationExtractor(asset_type_extractor)
        asset_decl_mapper = AssetDeclarationMapper(asset_extractor) 

        prop_mapper = DeclarationPropMapper(asset_type_extractor)
        event_decl_mapper = EventDeclarationMapper(prop_mapper)

        domain_mapper = DeclarationToDomainMapper()

        return NewEventNodeUpdater(
            asset_decl_mapper,
            event_decl_mapper,
            domain_mapper
        )
