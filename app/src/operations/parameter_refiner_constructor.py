from app.classes.operations.dependencies import Dependencies

from app.src.operations.parameter_refiner import ParameterRefiner
from app.src.pattern_builder.pattern_builder_builder import PatternBuilderBuilder

from app.src.update_processor.asset_declaration_extractor import AssetDeclarationExtractor
from app.src.update_processor.asset_declaration_mapper import AssetDeclarationMapper
from app.src.update_processor.event_declaration_mapper_builder import EventDeclarationMapperBuilder 
from app.src.update_processor.domain_model_mapper import DeclarationToDomainMapper

from app.src.update_processor.pattern_handlers.pattern_handler_dict_builder import PatternHandlerDictBuilder
from app.src.update_processor.domain_update_extractor import DomainUpdateExtractor
from app.src.update_processor.norm_update_extractor import NormUpdateExtractor
from app.src.update_processor.update_processor import UpdateProcessor

class ParameterRefinerConstructor:
    @staticmethod
    def construct(deps: Dependencies) -> ParameterRefiner:
        pattern_builder = PatternBuilderBuilder.build()

        asset_extractor = AssetDeclarationExtractor()
        asset_declaration_mapper = AssetDeclarationMapper(asset_extractor)
        event_declaration_mapper = EventDeclarationMapperBuilder.build()
        domain_mapper = DeclarationToDomainMapper()
        declaration_extractor = DomainUpdateExtractor(asset_declaration_mapper, event_declaration_mapper, domain_mapper)

        handler_dict = PatternHandlerDictBuilder.build()
        norm_update_extractor = NormUpdateExtractor(handler_dict)
        update_processor = UpdateProcessor(declaration_extractor, norm_update_extractor)

        return ParameterRefiner(pattern_builder, update_processor)
