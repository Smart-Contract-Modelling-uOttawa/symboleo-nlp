from typing import DefaultDict
from collections import defaultdict
from app.classes.units.all_units import *

from app.src.grammar_builder.unit_builders.unit_builder import IBuildUnit, DefaultUnitBuilder
from app.src.grammar_builder.unit_builders.subject_ub import SubjectUB
from app.src.grammar_builder.unit_builders.dobj_ub import DobjUB
from app.src.grammar_builder.unit_builders.time_unit_ub import TimeUnitUB
from app.src.grammar_builder.unit_builders.contract_action_ub import ContractActionUB
from app.src.grammar_builder.unit_builders.linking_verb_ub import LinkingVerbUB
from app.src.grammar_builder.unit_builders.time_period_ub import TimePeriodUB
from app.src.grammar_builder.unit_builders.notifier_unit_ub import NotifierUnitUB


class UnitBuilderDictConstructor:
    @staticmethod
    def build() -> DefaultDict[UnitType, IBuildUnit]:
        d = defaultdict(lambda: DefaultUnitBuilder())

        d[UnitType.SUBJECT] = SubjectUB()
        d[UnitType.DOBJ] = DobjUB()
        d[UnitType.CONTRACT_ACTION] = ContractActionUB()
        d[UnitType.TIME_UNIT] = TimeUnitUB()
        d[UnitType.LINKING_VERB] = LinkingVerbUB()
        d[UnitType.TIME_PERIOD] = TimePeriodUB()
        d[UnitType.NOTIFIER] = NotifierUnitUB()


        return d