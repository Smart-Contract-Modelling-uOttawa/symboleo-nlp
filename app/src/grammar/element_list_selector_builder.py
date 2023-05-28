from app.classes.operations.dependencies import Dependencies

from app.src.grammar.manual_token_selector import ManualTokenSelector
from app.src.grammar.input_converter import InputConverter
from app.src.grammar.value_getter import ValueGetter

from app.src.grammar.child_getter import ChildGetter
from app.src.extractors.value_extractor_dict_builder import ValueExtractorDictBuilder
from app.src.child_getters.child_getter_dict import ChildGetterDictConstructor

from app.src.grammar.element_list_selector import ElementListSelector


class ElementListSelectorBuilder:
    @staticmethod
    def build(deps: Dependencies):
        child_getter_dict = ChildGetterDictConstructor.build()
        child_getter = ChildGetter(child_getter_dict)

        child_selector = ManualTokenSelector()

        input_value_getter = ValueGetter()

        extractor_dict = ValueExtractorDictBuilder.build(deps)
        element_extractor = InputConverter(extractor_dict)
        #common_event_handler = CommonEventHandler()
        
        return ElementListSelector(
            child_getter,
            child_selector,
            input_value_getter,
            element_extractor
        )