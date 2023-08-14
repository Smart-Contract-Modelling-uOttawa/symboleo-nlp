
from app.classes.operations.dependencies import Dependencies
from app.src.operations.pattern_class_resolver import PatternClassResolver
from app.src.pattern_builder.pattern_builder_constructor import PatternBuilderConstructor

from app.src.norm_update_extractor.handlers.norm_update_handler_dict import NormUpdateHandlerDictBuilder
from app.src.norm_update_extractor.norm_update_extractor import NormUpdateExtractor
from app.src.domain_update_extractor.domain_update_extractor_builder import DomainUpdateExtractorBuilder
from app.src.operations.operation_mapper import OperationMapper

class OperationMapperBuilder:
    @staticmethod
    def build(deps: Dependencies):
        pattern_class_builder = PatternBuilderConstructor.construct(deps)

        pattern_class_resolver = PatternClassResolver()

        handler_dict = NormUpdateHandlerDictBuilder.build()
        norm_update_extractor = NormUpdateExtractor(handler_dict)

        domain_update_extractor = DomainUpdateExtractorBuilder.build(deps)

        result = OperationMapper(
            pattern_class_builder, 
            pattern_class_resolver,
            norm_update_extractor, 
            domain_update_extractor
        )

        return result

