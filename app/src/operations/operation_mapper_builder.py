
from app.classes.operations.dependencies import Dependencies
from app.src.pattern_builder.pattern_class_filler import PatternClassFiller
from app.src.pattern_builder.pattern_class_extractor import PatternClassExtractor
from app.src.pattern_builder.pattern_class_getter import AllPatternClassGetter
from app.src.pattern_builder.pattern_class_builder import PatternClassBuilder
from app.src.operations.pattern_class_resolver import PatternClassResolver
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler_dict import PatternUnitFillerDictConstructor

from app.src.norm_update_extractor.handlers.norm_update_handler_dict import NormUpdateHandlerDictBuilder
from app.src.norm_update_extractor.norm_update_extractor import NormUpdateExtractor
from app.src.domain_update_extractor.domain_update_extractor_builder import DomainUpdateExtractorBuilder
from app.src.operations.operation_mapper import OperationMapper

class OperationMapperBuilder:
    @staticmethod
    def build(deps: Dependencies):

        pattern_class_getter = AllPatternClassGetter()
        pattern_class_extractor = PatternClassExtractor(pattern_class_getter)
        pattern_filler_dict= PatternUnitFillerDictConstructor.build(deps)
        pattern_class_filler = PatternClassFiller(pattern_filler_dict)
        pattern_class_builder = PatternClassBuilder(pattern_class_extractor, pattern_class_filler)

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

