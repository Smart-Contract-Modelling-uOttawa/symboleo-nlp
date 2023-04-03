# Common dependencies - move to a script
from app.src.grammar.grammar_generator import GrammarGenerator
from app.src.grammar.grammar_config import GrammarGeneratorConfig
from app.src.grammar.grammar_selector import GrammarSelector
from app.src.grammar.helpers.domain_timepoint_extractor import DomainTimepointExtractor
from app.src.user_scripts.manual_node_selector import ManualGrammarNodeSelector

from app.src.operations.parameter_refiner import ParameterRefiner
from app.src.frames.frame_checker_constuctor import FrameCheckerConstructor
from app.src.operations.termination_updater import TerminationUpdater
from app.src.operations.domain_updater import DomainUpdater


class UserDependencies:
    def __init__(
            self,
            grammar_generator: GrammarGenerator,
            grammar_selector: GrammarSelector,
            parm_refiner: ParameterRefiner,
            tp_adder: TerminationUpdater,
            domain_updater: DomainUpdater,
    ):
        self.gg = grammar_generator
        self.gs = grammar_selector
        self.parm_refiner = parm_refiner
        self.tp_adder = tp_adder
        self.domain_updater = domain_updater
       

def get_dependencies() -> UserDependencies:
    domain_timepoint_extractor = DomainTimepointExtractor()
    gg = GrammarGenerator(domain_timepoint_extractor)

    inner_selector = ManualGrammarNodeSelector()
    gs = GrammarSelector(inner_selector)

    frame_checker = FrameCheckerConstructor.construct()
    parm_refiner = ParameterRefiner(frame_checker)
    tp_adder = TerminationUpdater(parm_refiner)
    domain_updater = DomainUpdater()

    return UserDependencies(gg, gs, parm_refiner, tp_adder, domain_updater)


