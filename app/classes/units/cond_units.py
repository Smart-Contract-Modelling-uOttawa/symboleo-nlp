from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

class ByGivingUnit(InputUnit):
    unit_type = UnitType.BY_GIVING
    prompt = 'By Giving'
    init_value = 'by giving'

class FollowingUnit(InputUnit):
    unit_type = UnitType.FOLLOWING
    prompt = 'Following'
    init_value = 'following'

class IfUnit(InputUnit):
    unit_type = UnitType.IF
    prompt = 'If'
    init_value = 'if'

class InCaseUnit(InputUnit):
    unit_type = UnitType.IN_CASE
    prompt = 'In case'
    init_value = 'in case'

class InEventUnit(InputUnit):
    unit_type = UnitType.IN_EVENT
    prompt = 'In the event that'
    init_value = 'in the event that'

class OnceUnit(InputUnit):
    unit_type = UnitType.ONCE
    prompt = 'Once'
    init_value = 'once'

class UponUnit(InputUnit):
    unit_type = UnitType.UPON
    prompt = 'Upon'
    init_value = 'upon'

class WhenUnit(InputUnit):
    unit_type = UnitType.WHEN
    prompt = 'When'
    init_value = 'when'