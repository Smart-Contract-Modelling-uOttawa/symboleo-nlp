from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.node_type import NodeType
from app.classes.units.input_unit import InputUnit
from app.classes.selection.selected_node import SelectedNode

from app.classes.template_event.common_event import CommonEvent

from app.src.grammar.common_event_handler import IHandleCommonEvents

class IProcessToken:
    def process(self, token: InputUnit, contract: ISymboleoContract) -> SelectedNode:
        raise NotImplementedError()


class CommonTokenProcessor(IProcessToken):
    def __init__(
        self,
        inner_processor: IProcessToken,
        common_event_handler: IHandleCommonEvents
    ):
        self.__common_event = None
        self.__inner_processor = inner_processor
        self.__common_event_handler = common_event_handler
        

    def process(self, token: InputUnit, contract: ISymboleoContract) -> SelectedNode:
        result = None
        fetched_val = None

        # Check if were in common situation and get the stored value
        if self.__common_event:
            fetched_val = self.__common_event_handler.handle(self.__common_event, token)
        
        if fetched_val:
            result = fetched_val
        else:
            result = self.__inner_processor.process(token, contract)
            # Check for common event and toggle if found
            if result.node_type == NodeType.COMMON_EVENT:
                self.toggle_common(result.value)
    
        return result


    def toggle_common(self, evt: CommonEvent):
        self.__common_event = evt

    def has_common(self):
        return self.__common_event is not None
