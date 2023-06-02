from __future__ import annotations
from typing import Dict, List
from app.classes.spec.domain_object import Asset, DomainEnum, DomainEvent, Role
from app.classes.helpers.list_eq import ClassHelpers

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
        self.roles: Dict[str, Role] = roles
        self.enums: List[DomainEnum] = enums
        self.events: Dict[str, DomainEvent] = events
        #self.aliases = aliases
        self.assets: Dict[str, Asset] = assets

    def __eq__(self, other: DomainModel) -> bool:
        return self.id == other.id and \
            ClassHelpers.dicts_eq(self.roles, other.roles) and \
            ClassHelpers.dicts_eq(self.events, other.events) and \
            ClassHelpers.dicts_eq(self.assets, other.assets) and \
            ClassHelpers.lists_eq(self.enums, other.enums, 'name')
        

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