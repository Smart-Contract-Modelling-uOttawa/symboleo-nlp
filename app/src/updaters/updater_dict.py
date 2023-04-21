from typing import DefaultDict, Type
from collections import defaultdict
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

# Ok for now, but if deps become shared, then will need to split it up
from app.src.updaters.new_event_node_updater_builder import NewEventNodeUpdaterBuilder

from app.src.operations.norm_builder import NormBuilder

# Can think of this as the SymboleoUpdater
class UpdaterDictConstructor:
    # Passing in dependencies..
    @staticmethod
    def build(deps) -> DefaultDict[Type[SelectedNode], IUpdatePackage]:
        # Set up injection... Will probably pull this out into the deps...
        norm_builder = NormBuilder()

        d = defaultdict(lambda: DefaultUpdater())

        d[RootNode] = RootNodeUpdater()
        d[BeforeNode] = BeforeNodeUpdater()
        d[IfNode] = IfNodeUpdater()
        d[NewEventNode] = NewEventNodeUpdaterBuilder.build()
        d[SubjectNode] = SubjectUpdater()
        d[VerbNode] = VerbUpdater()
        d[AdverbNode] = AdverbUpdater()
        d[PrepNode] = PPUpdater()
        d[DobjNode] = DobjUpdater()
        d[PredicateNode] = PredicateUpdater()
        d[StandardEventNode] = StandardEventNodeUpdater()
        d[ContractActionNode] = ContractActionNodeUpdater()
        d[ContractSubjectNode] = ContractSubjectNodeUpdater()
        d[DateNode] = DateNodeUpdater()
        d[DomainTimepointNode] = DomainTimePointNodeUpdater()
        d[TimespanNode] = TimespanNodeUpdater()
        d[WithinNode] = WithinNodeUpdater()
        d[UntilNode] = UntilNodeUpdater(norm_builder)

        return d