from typing import DefaultDict, Type
from collections import defaultdict
from app.classes.selection.selected_node import SelectedNode
from app.src.sym_updaters.package_updater import IUpdatePackage, DefaultUpdater
from app.classes.selection.all_nodes import *

from app.src.sym_updaters.root_node_updater import RootNodeUpdater
from app.src.sym_updaters.before_node_updater import BeforeNodeUpdater
from app.src.sym_updaters.if_node_updater import IfNodeUpdater
from app.src.sym_updaters.custom_event.custom_event_node_updater import CustomEventNodeUpdater
from app.src.sym_updaters.contract_subject_node_updater import ContractSubjectNodeUpdater
from app.src.sym_updaters.obligation_subject_node_updater import ObligationSubjectNodeUpdater
from app.src.sym_updaters.standard_event_node_updater import StandardEventNodeUpdater
from app.src.sym_updaters.domain_timepoint_node_updater import DomainTimePointNodeUpdater
from app.src.sym_updaters.timespan_node_updater import TimespanNodeUpdater
from app.src.sym_updaters.within_node_updater import WithinNodeUpdater
from app.src.sym_updaters.until_node_updater import UntilNodeUpdater
from app.src.sym_updaters.date_node_updater import DateNodeUpdater
from app.src.sym_updaters.custom_event.custom_event_component_updaters import *

from app.src.sym_updaters.leaf_node_updater import LeafNodeUpdater

# Ok for now, but if deps become shared, then will need to split it up
from app.src.sym_updaters.custom_event.cenu_builder import CustomEventNodeUpdaterBuilder

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
        d[CustomEventNode] = CustomEventNodeUpdaterBuilder.build()
        d[SubjectNode] = SubjectUpdater()
        d[VerbNode] = VerbUpdater()
        d[AdverbNode] = AdverbUpdater()
        d[PrepNode] = PPUpdater()
        d[DobjNode] = DobjUpdater()
        d[PredicateNode] = PredicateUpdater()
        #d[StandardEventNode] = StandardEventNodeUpdater()
        d[DateNode] = DateNodeUpdater()
        d[DomainTimepointNode] = DomainTimePointNodeUpdater()
        d[TimespanNode] = TimespanNodeUpdater()
        d[WithinNode] = WithinNodeUpdater()
        d[UntilNode] = UntilNodeUpdater(norm_builder)

        d[ContractActionNode] = LeafNodeUpdater()
        d[ContractSubjectNode] = ContractSubjectNodeUpdater()
        d[ObligationActionNode] = LeafNodeUpdater()
        d[ObligationSubjectNode] = ObligationSubjectNodeUpdater()

        return d