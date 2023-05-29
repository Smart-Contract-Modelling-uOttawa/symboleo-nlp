from app.src.operations.contract_updater import ContractUpdater
from app.src.operations.domain_updater import DomainUpdater
from app.src.operations.termination_updater import TerminationUpdater
from app.src.grammar.element_extractor_builder import ElementExtractorBuilder
from app.src.operations.refine_parameter.parameter_refiner_constructor import ParameterRefinerConstructor
from app.src.extractors.value_extractor_dict_builder import ValueExtractorDictBuilder

from app.src.grammar.element_extractor import ElementExtractor
from app.src.operations.dependency_builder import DependencyBuilder

class ContractUpdaterBuilder:
    @staticmethod
    def build() -> ContractUpdater:
        deps = DependencyBuilder.build(fake=True)
        element_extractor = ElementExtractorBuilder.build(deps)
        

        parm_refiner = ParameterRefinerConstructor.construct(deps)
        tp_adder = TerminationUpdater(parm_refiner)
        do_adder = DomainUpdater()

        return ContractUpdater(element_extractor, parm_refiner, tp_adder, do_adder)