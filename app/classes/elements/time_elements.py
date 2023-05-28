from app.classes.elements.element import Element
from app.classes.other.timespan import Timespan
from app.classes.units.unit_type import UnitType

class TimespanElement(Element[Timespan]):
    unit_type = UnitType.TIMESPAN

class TimepointElement(Element[str]):
    unit_type = UnitType.TIMEPOINT

class DomainTimepointElement(Element[str]):
    unit_type = UnitType.DOMAIN_TIMEPOINT

class DateElement(Element[str]):
    unit_type = UnitType.DATE
