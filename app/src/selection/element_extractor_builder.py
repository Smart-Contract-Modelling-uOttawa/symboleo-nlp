from app.src.selection.element_extractor import ElementExtractor
from app.src.selection.element_extractors.element_extractor_dict_builder import ElementExtractorDictBuilder
from app.classes.operations.dependencies import Dependencies

class ElementExtractorBuilder:
    @staticmethod
    def build(deps: Dependencies):
        extractor_dict = ElementExtractorDictBuilder.build(deps)
        
        return ElementExtractor(extractor_dict)