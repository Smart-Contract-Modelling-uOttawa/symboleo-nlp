from app.classes.operations.dependencies import Dependencies

#from app.src.operations.refine_parameter.parameter_refiner import ParameterRefiner
from app.src.operations.refine_parameter.parameter_refiner_new import ParameterRefiner
from app.src.frame_updaters.frame_builder_builder import FrameBuilderBuilder
from app.src.sym_updaters.sym_updater_dict import SymUpdaterDictConstructor
from app.src.sym_updaters.update_extractor import UpdateExtractor

from app.src.sym_updaters.custom_event.asset_decl_extractor import AssetDeclarationExtractor
from app.src.sym_updaters.custom_event.asset_declaration_mapper import AssetDeclarationMapper
from app.src.sym_updaters.custom_event.event_declaration_mapper_builder import EventDeclarationMapperBuilder 
from app.src.sym_updaters.custom_event.domain_model_mapper import DeclarationToDomainMapper

from app.src.update_processor.pattern_handlers.pattern_handler_dict_builder import PatternHandlerDictBuilder
from app.src.update_processor.domain_update_extractor import DomainUpdateExtractor
from app.src.update_processor.norm_update_extractor import NormUpdateExtractor
from app.src.update_processor.update_processor import UpdateProcessor

class ParameterRefinerConstructor:
    @staticmethod
    def construct(deps: Dependencies) -> ParameterRefiner:
        frame_builder = FrameBuilderBuilder.build()
        #updater_dict = SymUpdaterDictConstructor.build(deps)
        #update_extractor = UpdateExtractor(updater_dict)

        asset_extractor = AssetDeclarationExtractor()
        asset_declaration_mapper = AssetDeclarationMapper(asset_extractor)
        event_declaration_mapper = EventDeclarationMapperBuilder.build()
        domain_mapper = DeclarationToDomainMapper()
        declaration_extractor = DomainUpdateExtractor(asset_declaration_mapper, event_declaration_mapper, domain_mapper)

        handler_dict = PatternHandlerDictBuilder.build()
        norm_update_extractor = NormUpdateExtractor(handler_dict)
        update_processor = UpdateProcessor(declaration_extractor, norm_update_extractor)

        return ParameterRefiner(frame_builder, update_processor)
