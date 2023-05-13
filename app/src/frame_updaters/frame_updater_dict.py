from typing import Type, DefaultDict
from collections import defaultdict
from app.classes.selection.selected_node import SelectedNode
from app.classes.selection.all_nodes import *


from app.src.frame_updaters.frame_updater import DefaultFrameUpdater, IUpdateFrame
from app.src.frame_updaters.contract_action import ContractActionUpdater
from app.src.frame_updaters.contract_subject import ContractSubjectUpdater
from app.src.frame_updaters.obligation_action_updater import ObligationActionUpdater
from app.src.frame_updaters.obligation_subject_updater import ObligationSubjectUpdater
from app.src.frame_updaters.date_node import DateUpdater
from app.src.frame_updaters.domain_timepoint_node import DomainTimepointUpdater
from app.src.frame_updaters.timespan_node import TimespanUpdater
from app.src.frame_updaters.after_node import AfterUpdater
from app.src.frame_updaters.custom_event_nodes import *

class FrameUpdaterDictConstructor:
    @staticmethod
    def build() -> DefaultDict[Type[SelectedNode], IUpdateFrame]:
        d = defaultdict(lambda: DefaultFrameUpdater())
        
        d[AfterNode] = AfterUpdater()

        d[DateNode] = DateUpdater()
        d[DomainTimepointNode] = DomainTimepointUpdater()
        d[TimespanNode] = TimespanUpdater()

        d[SubjectNode] = SubjectUpdater()
        d[VerbNode] = VerbUpdater()
        d[PredicateNode] = PredicateUpdater()
        d[DobjNode] = DobjUpdater()
        d[AdverbNode] = AdverbUpdater()
        d[PrepNode] = PrepPhraseUpdater()

        d[ContractActionNode] = ContractActionUpdater()
        d[ContractSubjectNode] = ContractSubjectUpdater()

        d[ObligationActionNode] = ObligationActionUpdater()
        d[ObligationSubjectNode] = ObligationSubjectUpdater()
    
        return d