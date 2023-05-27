from typing import List, Dict, Type
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.selection.selected_node import SelectedNode
from app.classes.units.node_type import NodeType
from app.classes.units.input_unit import InputUnit
from app.classes.custom_event.custom_event import CustomEvent
from app.classes.template_event.common_event import CommonEvent

from app.src.grammar.input_converter import IConvertInput
from app.classes.units.root_node import RootNode

from app.src.child_getters.child_getter import IGetNodeChildren
from app.src.grammar.value_getter import IGetValues

from app.classes.selection.custom_event_node import *
from app.classes.selection.final_node import FinalNode
#...

from app.classes.template_event.common_event_dict import COMMON_EVENT_DICT

# Kill this.
class ISelectGrammar:
    def select(self):
        raise NotImplementedError()

class ISelectGrammarNodes:
    def select(self, node_set: List[InputUnit]) -> InputUnit:
        raise NotImplementedError()


class GrammarSelector(ISelectGrammar):
    def __init__(
        self, 
        child_getter_dict: Dict[Type[InputUnit], IGetNodeChildren],
        value_getter: IGetValues,
        input_converter: IConvertInput,
        inner_selector: ISelectGrammarNodes
    ):
        self.__child_getter_dict = child_getter_dict
        self.__value_getter = value_getter
        self.__input_converter = input_converter
        self.__inner_selector = inner_selector

    def select(self, contract: ISymboleoContract) -> List[SelectedNode]:
        curr = RootNode()
        results: List[SelectedNode] = [curr.sn_type()]
        next_result = None

        common_event = None

        # Will abstract this away and clean it up to be testable
        while (True):
            op = self.__child_getter_dict[type(curr)]
            next_set = op.get(curr, contract, next_result)
            if len(next_set) == 0: 
                break

            curr = self.__inner_selector.select(next_set)

            fetched_val = None
            if common_event:
                fetched_val = self._handle_common_event(common_event, curr)
            
            if fetched_val:
                next_result = fetched_val
            else:
                user_input = self.__value_getter.get(curr)
                next_result = self.__input_converter.convert([user_input])[0]
            
            results.append(next_result)

            if curr.node_type == NodeType.COMMON_EVENT:
                common_event = COMMON_EVENT_DICT[user_input.value]
            
        return results


    def _handle_common_event(self, evt: CommonEvent, curr: InputUnit):
        if curr.node_type == NodeType.SUBJECT:
            if evt.subj:
                return SubjectNode(evt.subj)

        if curr.node_type == NodeType.VERB:
            return VerbNode(evt.verb)

        if curr.node_type == NodeType.DOBJ:
            return DobjNode(evt.dobj)
        
        if curr.node_type == NodeType.ADVERB:
            return AdverbNode(evt.adverb)
        
        if curr.node_type == NodeType.FINAL_NODE:
            return FinalNode(CommonEvent(common_event_key=evt.common_event_key))
        
        return None
