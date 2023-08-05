from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType, UnitVariety

class FollowingUnit(InputUnit):
    unit_type = UnitType.FOLLOWING
    unit_var = UnitVariety.STATIC
    prompt = 'Following'
    init_value = 'following'

class IfUnit(InputUnit):
    unit_type = UnitType.IF
    unit_var = UnitVariety.STATIC
    prompt = 'If'
    init_value = 'if'

class InCaseUnit(InputUnit):
    unit_type = UnitType.IN_CASE
    unit_var = UnitVariety.STATIC
    prompt = 'In case'
    init_value = 'in case'

class InEventUnit(InputUnit):
    unit_type = UnitType.IN_EVENT
    unit_var = UnitVariety.STATIC
    prompt = 'In the event that'
    init_value = 'in the event that'

class OnceUnit(InputUnit):
    unit_type = UnitType.ONCE
    unit_var = UnitVariety.STATIC
    prompt = 'Once'
    init_value = 'once'

class UponUnit(InputUnit):
    unit_type = UnitType.UPON
    unit_var = UnitVariety.STATIC
    prompt = 'Upon'
    init_value = 'upon'

class WhenUnit(InputUnit):
    unit_type = UnitType.WHEN
    unit_var = UnitVariety.STATIC
    prompt = 'When'
    init_value = 'when'