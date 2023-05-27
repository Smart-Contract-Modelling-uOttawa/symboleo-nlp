from app.src.grammar.input_converter import InputConverter
from app.src.extractors.value_extractor_dict_builder import ValueExtractorDictBuilder
from app.classes.operations.dependencies import Dependencies

class InputConverterBuilder:
    @staticmethod
    def build(deps: Dependencies):
        extractor_dict = ValueExtractorDictBuilder.build(deps)
        
        return InputConverter(extractor_dict)