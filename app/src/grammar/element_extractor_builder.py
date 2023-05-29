from app.src.grammar.element_extractor import ElementExtractor
from app.src.extractors.value_extractor_dict_builder import ValueExtractorDictBuilder
from app.classes.operations.dependencies import Dependencies

class ElementExtractorBuilder:
    @staticmethod
    def build(deps: Dependencies):
        extractor_dict = ValueExtractorDictBuilder.build(deps)
        
        return ElementExtractor(extractor_dict)