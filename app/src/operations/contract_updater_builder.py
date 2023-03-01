from app.src.operations.predicate_refiner import PredicateRefiner
from app.src.operations.trigger_adder import TriggerAdder
from app.src.operations.dm_prop_adder import DomainPropAdder
from app.src.operations.norm_adder import NormAdder
from app.src.operations.contract_updater import ContractUpdater
from app.src.operations.helpers.norm_proposition_updater import NormPropositionUpdater
from app.src.operations.helpers.predicate_processor import PredicateProcessor

class ContractUpdaterBuilder:
    @staticmethod
    def build() -> ContractUpdater:
        norm_proposition_updater = NormPropositionUpdater()
        predicate_processor = PredicateProcessor(norm_proposition_updater)
        predicate_refiner = PredicateRefiner(predicate_processor)
        trigger_adder = TriggerAdder(predicate_processor)
        norm_adder = NormAdder()
        dm_prop_adder = DomainPropAdder()

        return ContractUpdater(
            predicate_refiner,
            trigger_adder,
            norm_adder,
            dm_prop_adder
        )

