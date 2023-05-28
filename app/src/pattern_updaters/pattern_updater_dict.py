from typing import Type, DefaultDict
from collections import defaultdict
from app.classes.elements.element import Element
from app.classes.elements.all_nodes import *


from app.src.pattern_updaters.pattern_updater import IUpdatePattern, DefaultPatternUpdater
from app.src.pattern_updaters.contract_action import ContractActionUpdater
from app.src.pattern_updaters.contract_subject import ContractSubjectUpdater
from app.src.pattern_updaters.obligation_action_updater import ObligationActionUpdater
from app.src.pattern_updaters.obligation_subject_updater import ObligationSubjectUpdater
from app.src.pattern_updaters.date_node import DateUpdater
from app.src.pattern_updaters.timespan_node import TimespanUpdater
from app.src.pattern_updaters.custom_event_nodes import *

class PatternUpdaterDictConstructor:
    @staticmethod
    def build() -> DefaultDict[Type[Element], IUpdatePattern]:
        d = defaultdict(lambda: DefaultPatternUpdater())
        
        #d[AfterNode] = AfterUpdater()

        d[DateNode] = DateUpdater()
        #d[DomainTimepointNode] = DomainTimepointUpdater()
        d[TimespanNode] = TimespanUpdater()

        d[SubjectNode] = SubjectUpdater()
        d[VerbNode] = VerbUpdater()
        d[FailsToNode] = FailsToUpdater()
        d[PredicateNode] = PredicateUpdater()
        d[DobjNode] = DobjUpdater()
        d[AdverbNode] = AdverbUpdater()
        d[PrepNode] = PrepPhraseUpdater()

        d[ContractActionNode] = ContractActionUpdater()
        d[ContractSubjectNode] = ContractSubjectUpdater()

        d[ObligationActionNode] = ObligationActionUpdater()
        d[ObligationSubjectNode] = ObligationSubjectUpdater()
    
        return d