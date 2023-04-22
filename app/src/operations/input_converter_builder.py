from app.src.operations.input_converter import InputConverter
from app.src.extractors.value_extractor import ValueExtractorDictBuilder
from app.classes.operations.dependencies import Dependencies

class InputConverterBuilder:
    @staticmethod
    def build(deps: Dependencies):
        extractor_dict = ValueExtractorDictBuilder.build(deps)

        return InputConverter(extractor_dict)