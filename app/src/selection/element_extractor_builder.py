from app.src.selection.element_extractor import ElementExtractor
from app.src.selection.element_extractors.value_extractor_dict_builder import ValueExtractorDictBuilder
from app.classes.operations.dependencies import Dependencies

class ElementExtractorBuilder:
    @staticmethod
    def build(deps: Dependencies):
        extractor_dict = ValueExtractorDictBuilder.build(deps)
        
        return ElementExtractor(extractor_dict)