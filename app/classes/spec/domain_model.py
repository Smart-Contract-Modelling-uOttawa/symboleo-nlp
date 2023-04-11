from app.classes.spec.domain_object import Asset, DomainEnum, DomainEvent, Role
from app.classes.spec._sd import _sd


from typing import Dict, List


class DomainModel:
    def __init__(
        self,
        id: str,
        roles: Dict[str, Role],
        enums: List[DomainEnum],
        events: Dict[str, DomainEvent],
        assets: Dict[str, Asset]
    ):
        self.id = id
        self.roles: Dict[str, Role] = _sd(roles)
        self.enums: List[DomainEnum] = sorted(enums, key=lambda x: x.name)
        self.events: Dict[str, DomainEvent] = _sd(events)
        #self.aliases = aliases
        self.assets: Dict[str, Asset] = _sd(assets)

    def to_sym(self):
        result = f'Domain {self.id}\n'
        for x in self.roles:
            result += f'  {self.roles[x].to_sym()}\n'

        for x in self.enums:
            result += f'  {x.to_sym()}\n'

        for x in self.assets:
            result += f'  {self.assets[x].to_sym()}\n'

        for x in self.events:
            result += f'  {self.events[x].to_sym()}\n'

        result += f'\nendDomain'

        return result