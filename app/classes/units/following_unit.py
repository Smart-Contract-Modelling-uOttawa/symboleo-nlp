from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.event_unit import EventUnit

class FollowingUnit(InputUnit):
    unit_type = UnitType.FOLLOWING
    prompt = 'Following'
    init_value = 'following'
    children = [EventUnit]
