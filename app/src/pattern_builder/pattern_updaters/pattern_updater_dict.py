from typing import Type, DefaultDict
from collections import defaultdict
from app.classes.elements.element import Element
from app.classes.elements.all_elements import *

from app.src.pattern_builder.pattern_updaters.pattern_updater import IUpdatePattern, DefaultPatternUpdater
from app.src.pattern_builder.pattern_updaters.contract_action_updater import ContractActionUpdater
from app.src.pattern_builder.pattern_updaters.obligation_action_updater import ObligationActionUpdater
from app.src.pattern_builder.pattern_updaters.obligation_subject_updater import ObligationSubjectUpdater
from app.src.pattern_builder.pattern_updaters.date_updater import DateUpdater
from app.src.pattern_builder.pattern_updaters.timespan_updater import TimespanUpdater
from app.src.pattern_builder.pattern_updaters.custom_event_updaters import *

class PatternUpdaterDictConstructor:
    @staticmethod
    def build() -> DefaultDict[Type[Element], IUpdatePattern]:
        d = defaultdict(lambda: DefaultPatternUpdater())
        
        #d[AfterElement] = AfterUpdater()

        d[DateElement] = DateUpdater()
        #d[DomainTimepointElement] = DomainTimepointUpdater()
        d[TimespanElement] = TimespanUpdater()

        d[SubjectElement] = SubjectUpdater()
        d[VerbElement] = VerbUpdater()
        d[FailsToElement] = FailsToUpdater()
        d[PredicateElement] = PredicateUpdater()
        d[DobjElement] = DobjUpdater()
        d[AdverbElement] = AdverbUpdater()
        d[PrepElement] = PrepPhraseUpdater()

        d[ContractActionElement] = ContractActionUpdater()

        d[ObligationActionElement] = ObligationActionUpdater()
        d[ObligationSubjectElement] = ObligationSubjectUpdater()
    
        return d