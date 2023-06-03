from app.classes.operations.dependencies import Dependencies

from app.src.selection.manual_token_selector import ManualNodeSelector
from app.src.selection.element_extractor import ElementExtractor
from app.src.selection.input_value_getter import InputValueGetter

from app.src.selection.child_node_getter import ChildNodeGetter
from app.src.selection.element_extractors.element_extractor_dict_builder import ElementExtractorDictBuilder
from app.src.selection.child_getters.child_getter_dict import ChildGetterDictConstructor

from app.src.selection.element_list_selector import ElementListSelector


class ElementListSelectorBuilder:
    @staticmethod
    def build(deps: Dependencies):
        child_getter_dict = ChildGetterDictConstructor.build()
        child_getter = ChildNodeGetter(child_getter_dict)

        child_selector = ManualNodeSelector()

        input_value_getter = InputValueGetter()

        extractor_dict = ElementExtractorDictBuilder.build(deps)
        element_extractor = ElementExtractor(extractor_dict)
        #common_event_handler = CommonEventHandler()
        
        return ElementListSelector(
            child_getter,
            child_selector,
            input_value_getter,
            element_extractor
        )