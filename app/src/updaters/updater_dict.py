from typing import Dict, Type
from app.classes.selection.selected_node import SelectedNode
from app.src.updaters.iupdate_package import IUpdatePackage, DefaultUpdater
from app.classes.selection.all_nodes import *

from app.src.updaters.root_node import RootNodeUpdater
from app.src.updaters.before_node import BeforeNodeUpdater
from app.src.updaters.if_node import IfNodeUpdater
from app.src.updaters.new_event_node import NewEventNodeUpdater
from app.src.updaters.contract_action_node import ContractActionNodeUpdater
from app.src.updaters.contract_subject_node import ContractSubjectNodeUpdater
from app.src.updaters.standard_event_node import StandardEventNodeUpdater
from app.src.updaters.domain_timepoint_node import DomainTimePointNodeUpdater
from app.src.updaters.timespan_node import TimespanNodeUpdater
from app.src.updaters.within_node import WithinNodeUpdater
from app.src.updaters.until_node import UntilNodeUpdater
from app.src.updaters.date_node import DateNodeUpdater
from app.src.updaters.new_event_nodes import *

from app.src.nlp.frame_event_mappers import DomainEventMapper, DeclarationEventMapper
from app.src.operations.norm_builder import NormBuilder

class UpdaterDictConstructor:
    @staticmethod
    def build() -> Dict[Type[SelectedNode], IUpdatePackage]:
        # Set up injection
        decl_mapper = DeclarationEventMapper()
        domain_mapper = DomainEventMapper()

        norm_builder = NormBuilder()

        # Can make a defaultdict as well with Defaultupdater...
        return {
            RootNode: RootNodeUpdater(),
            BeforeNode: BeforeNodeUpdater(),
            IfNode: IfNodeUpdater(),
            EventNode: DefaultUpdater(),
            NewEventNode: NewEventNodeUpdater(decl_mapper, domain_mapper),
            SubjectNode: SubjectUpdater(),
            VerbNode: VerbUpdater(),
            AdverbNode: AdverbUpdater(),
            PrepNode: PPUpdater(),
            DobjNode: DobjUpdater(),
            PredicateNode: PredicateUpdater(),
            StandardEventNode: StandardEventNodeUpdater(),
            ContractActionNode: ContractActionNodeUpdater(),
            ContractSubjectNode: ContractSubjectNodeUpdater(),
            DateNode: DateNodeUpdater(),
            DomainTimepointNode: DomainTimePointNodeUpdater(),
            TimepointNode: DefaultUpdater(),
            TimespanNode: TimespanNodeUpdater(),
            WithinNode: WithinNodeUpdater(),
            UntilNode: UntilNodeUpdater(norm_builder)
        }