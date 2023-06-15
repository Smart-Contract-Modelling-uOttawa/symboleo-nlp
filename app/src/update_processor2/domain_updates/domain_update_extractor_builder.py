
from app.classes.operations.dependencies import Dependencies

from app.src.update_processor2.domain_updates.domain_update_extractor import DomainUpdateExtractor

from app.src.update_processor2.domain_updates.asset_declaration_extractor import AssetDeclarationExtractor
from app.src.update_processor2.domain_updates.asset_declaration_mapper import AssetDeclarationMapper

from app.src.update_processor2.domain_updates.event_declaration_mapper import EventDeclarationMapper
from app.src.update_processor.declaration_prop_mapper import DeclarationPropMapper

from app.src.update_processor2.domain_updates.domain_model_mapper import DeclarationToDomainMapper

from app.src.update_processor2.domain_updates.custom_event_extractor_builder import CustomEventExtractorBuilder

class DomainUpdateExtractorBuilder:

    @staticmethod
    def build(deps: Dependencies):
        asset_extractor = AssetDeclarationExtractor()
        asset_decl_mapper = AssetDeclarationMapper(asset_extractor)

        prop_mapper = DeclarationPropMapper()
        event_decl_mapper = EventDeclarationMapper(prop_mapper)

        domain_mapper = DeclarationToDomainMapper()

        custom_event_extractor = CustomEventExtractorBuilder.build(deps)

        return DomainUpdateExtractor(
            asset_decl_mapper,
            event_decl_mapper,
            domain_mapper,
            custom_event_extractor
        )