from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

class ObligationActionUnit(InputUnit):
    unit_type = UnitType.OBLIGATION_ACTION
    prompt = 'Obligation Action'
    needs_value = True

class ObligationSubjectUnit(InputUnit):
    unit_type = UnitType.OBLIGATION_SUBJECT
    prompt = 'Obligation Subject'
    needs_value = True


class ContractActionUnit(InputUnit):
    unit_type = UnitType.CONTRACT_ACTION
    prompt = 'Contract Action'
    needs_value = True

class ContractSubjectUnit(InputUnit):
    unit_type = UnitType.CONTRACT_SUBJECT
    prompt = 'Contract Subject'

class ContractEventUnit(InputUnit):
    unit_type = UnitType.CONTRACT_EVENT
    prompt = 'Contract Event'

class NormEventUnit(InputUnit):
    unit_type = UnitType.NORM_EVENT
    prompt = 'Norm Event'
    needs_value = True

