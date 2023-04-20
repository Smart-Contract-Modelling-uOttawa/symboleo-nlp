# Common dependencies - move to a script
from app.src.grammar.grammar_graph import GrammarGraph
from app.src.grammar.value_getter import ValueGetter
from app.src.grammar.grammar_selector import GrammarSelector
from app.src.user_scripts.manual_node_selector import ManualGrammarNodeSelector

from app.src.operations.input_converter_builder import InputConverterBuilder
from app.src.operations.refine_parameter2.parameter_refiner_constructor import ParameterRefinerConstructor
from app.src.operations.refine_parameter2.parameter_refiner import ParameterRefiner
from app.src.operations.add_power.termination_updater import TerminationUpdater
from app.src.operations.domain_updater import DomainUpdater

from app.src.operations.dependencies import Dependencies

class UserDependencies:
    def __init__(
            self,
            grammar_selector: GrammarSelector,
            parm_refiner: ParameterRefiner,
            tp_adder: TerminationUpdater,
            domain_updater: DomainUpdater
    ):
        self.gs = grammar_selector
        self.parm_refiner = parm_refiner
        self.tp_adder = tp_adder
        self.domain_updater = domain_updater


# Need NLP
def get_dependencies(nlp) -> UserDependencies:
    deps = Dependencies(nlp)
    
    # Not in use.. Will need this somewhere...
    #domain_timepoint_extractor = DomainTimepointExtractor()
    
    grammar_graph = GrammarGraph()
    value_getter = ValueGetter()
    input_converter = InputConverterBuilder.build(deps)
    inner_selector = ManualGrammarNodeSelector()

    gs = GrammarSelector(grammar_graph, value_getter, input_converter, inner_selector)

    parm_refiner = ParameterRefinerConstructor.construct(deps)
    tp_adder = TerminationUpdater(parm_refiner)
    domain_updater = DomainUpdater()

    return UserDependencies(gs, parm_refiner, tp_adder, domain_updater)


