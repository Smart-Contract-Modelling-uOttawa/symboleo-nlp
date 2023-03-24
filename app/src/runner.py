from app.classes.symboleo_contract import SymboleoContract
from app.src.operations.parm_operations.configs import ParameterConfig
from app.classes.grammar.grammar_nodes.root_node import RootNode
from app.classes.spec.sym_event import SymEvent
from app.classes.frames.frame import Frame
from app.classes.grammar.selected_node import Basket

from app.src.grammar.selection import Selection
from app.src.operations.helpers.default_event_getter import DefaultEventGetter
from app.src.frames.frame_checker_constuctor import FrameCheckerConstructor
from app.src.operations.parm_operations.parameter_updater_builder import ParameterUpdaterBuilder

class Runner:
    def __init__(self, contract: SymboleoContract, parm_config: ParameterConfig):
        self.contract = contract
        self.parm_config = parm_config
    

    def update_contract(self, selection: Selection):
        frame = self._get_frame(selection)

        basket = Basket()
        basket.default_event = self._extract_default_event()
        basket.initial_norm = self.contract.contract_spec.__dict__[self.parm_config.norm_type][self.parm_config.norm_id]
        symboleo_obj = selection.to_obj(basket)

        contract_updater = ParameterUpdaterBuilder.build()
        updated_contract = contract_updater.update(frame.op_code, self.contract, symboleo_obj, self.parm_config)
        return updated_contract


    def _get_frame(self, selection: Selection) -> Frame:
        frame_checker = FrameCheckerConstructor.construct()
        frames = frame_checker.check_all_frames(selection.nodes)
        # for x in frames:
        #     print(type(x), x.to_text())
        main_frame = frames[0]
        return main_frame


    def _extract_default_event(self, ) -> SymEvent:
        deg = DefaultEventGetter()
        default_event = deg.get(self.contract.contract_spec, self.parm_config)
        return default_event