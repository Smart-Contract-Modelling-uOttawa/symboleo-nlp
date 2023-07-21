from app.classes.operations.dependencies import Dependencies

from app.console_app.parm_getter import IGetParm, ParmGetter

from app.console_app.input_converter import InputConverter
from app.console_app.selector import InputSelector, ISelectInput

from app.src.grammar_builder.grammar_builder_constructor import GrammarBuilderConstructor
from app.src.grammar_builder.grammar_builder import IBuildGrammar

from app.src.operations.contract_updater_builder import ContractUpdaterBuilder
from app.src.operations.contract_updater import IUpdateContract

class ConsoleDependencies:
    def __init__(
            self,
            parm_getter: IGetParm,
            grammar_builder: IBuildGrammar,
            selector: ISelectInput,
            contract_updater: IUpdateContract
    ):
        self.parm_getter = parm_getter
        self.grammar_builder = grammar_builder
        self.selector = selector
        self.contract_updater = contract_updater

def get_dependencies(deps: Dependencies) -> ConsoleDependencies:
    parm_getter = ParmGetter()

    grammar_builder = GrammarBuilderConstructor.construct()

    input_converter = InputConverter()
    selector = InputSelector(input_converter)

    contract_updater = ContractUpdaterBuilder.build(deps)

    return ConsoleDependencies(
        parm_getter,
        grammar_builder,
        selector,
        contract_updater
    )


