from app.classes.operations.dependencies import Dependencies

from app.src.operations.refine_parameter.parameter_refiner_constructor import ParameterRefinerConstructor
from app.src.operations.refine_parameter.parameter_refiner import ParameterRefiner
from app.src.operations.termination_updater import TerminationUpdater
from app.src.operations.domain_updater import DomainUpdater

from app.src.grammar.grammar_selector_builder import GrammarSelectorBuilder
from app.src.grammar.grammar_selector2 import GrammarSelector

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


def get_dependencies(deps: Dependencies) -> UserDependencies:
    gs = GrammarSelectorBuilder.build(deps)

    parm_refiner = ParameterRefinerConstructor.construct(deps)
    
    tp_adder = TerminationUpdater(parm_refiner)
    
    domain_updater = DomainUpdater()

    return UserDependencies(gs, parm_refiner, tp_adder, domain_updater)


