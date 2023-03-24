from app.classes.symboleo_contract import SymboleoContract
from app.src.operations.parm_operations.configs import ParameterConfig
from app.src.operations.parm_operations.parameter_updater import ParameterOperation
from app.src.grammar.selection import Selection

from app.classes.grammar.selected_node import Basket
from app.src.grammar.selection import Selection
from app.src.operations.helpers.default_event_getter import IGetDefaultEvents
from app.src.frames.frame_checker import FrameChecker, ICheckFrames

class IExtractParameterOperation:
    def extract(self, contract: SymboleoContract, parm_config: ParameterConfig, selection: Selection) -> ParameterOperation:
        raise NotImplementedError()


class ParameterOperationExtractor(IExtractParameterOperation):
    def __init__(
            self, 
            frame_checker: ICheckFrames,
            default_event_getter: IGetDefaultEvents
        ):
        self.__frame_checker = frame_checker
        self.__default_event_getter = default_event_getter
    
    def extract(self, contract: SymboleoContract, parm_config: ParameterConfig, selection: Selection) -> ParameterOperation:
        frames = self.__frame_checker.check_all_frames(selection.nodes)
        frame = frames[0]
    
        basket = Basket()
        basket.default_event = self.__default_event_getter.get(contract.contract_spec, parm_config)
        basket.initial_norm = contract.contract_spec.__dict__[parm_config.norm_type][parm_config.norm_id]
        update_obj = selection.to_obj(basket)

        return ParameterOperation(frame.op_code, parm_config, update_obj)