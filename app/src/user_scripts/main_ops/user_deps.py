# Common dependencies - move to a script
from app.src.grammar.grammar_generator import GrammarGenerator
from app.src.grammar.grammar_config import GrammarGeneratorConfig
from app.src.grammar.grammar_selector import GrammarSelector
from app.src.grammar.helpers.domain_timepoint_extractor import DomainTimepointExtractor
from app.src.user_scripts.manual_node_selector import ManualGrammarNodeSelector

from app.src.operations.parm_operations.parameter_updater import ParmOpCode, ParameterConfig
from app.src.operations.parm_operations.parameter_operation_extractor import ParameterOperationExtractor
from app.src.frames.frame_checker_constuctor import FrameCheckerConstructor
from app.src.operations.helpers.default_event_getter import DefaultEventGetter

class UserDependencies:
    def __init__(
            self,
            grammar_generator: GrammarGenerator,
            grammar_selector: GrammarSelector,
            parm_op_extractor: ParameterOperationExtractor
    ):
        self.gg = grammar_generator
        self.gs = grammar_selector
        self.poe = parm_op_extractor

def get_dependencies() -> UserDependencies:
    domain_timepoint_extractor = DomainTimepointExtractor()
    gg = GrammarGenerator(domain_timepoint_extractor)

    inner_selector = ManualGrammarNodeSelector()
    gs = GrammarSelector(inner_selector)

    frame_checker = FrameCheckerConstructor.construct()
    deg = DefaultEventGetter()
    poe = ParameterOperationExtractor(frame_checker, deg)

    return UserDependencies(gg, gs, poe)


