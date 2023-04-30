from app.classes.operations.dependencies import Dependencies

from app.src.grammar.grammar_selector2 import GrammarSelector

from app.src.grammar.token_selector import TokenSelector
from app.src.grammar.manual_token_selector import ManualTokenSelector
from app.src.grammar.token_processor import CommonTokenProcessor
from app.src.grammar.simple_token_processor import SimpleTokenProcessor
from app.src.grammar.input_converter import InputConverter
from app.src.grammar.value_getter import ValueGetter
from app.src.grammar.common_event_handler import CommonEventHandler

from app.src.extractors.value_extractor_dict_builder import ValueExtractorDictBuilder
from app.src.child_getters.child_getter_dict import ChildGetterDictConstructor



class GrammarSelectorBuilder:
    @staticmethod
    def build(deps: Dependencies):
        child_getter_dict = ChildGetterDictConstructor.build()
        extractor_dict = ValueExtractorDictBuilder.build(deps)

        inner_selector = ManualTokenSelector()
        token_selector = TokenSelector(child_getter_dict, inner_selector)

        value_getter = ValueGetter()
        input_converter = InputConverter(extractor_dict)
        inner_processor = SimpleTokenProcessor(value_getter, input_converter)
        common_event_handler = CommonEventHandler()
        token_processor = CommonTokenProcessor(inner_processor, common_event_handler)

        return GrammarSelector(
            token_selector,
            token_processor
        )