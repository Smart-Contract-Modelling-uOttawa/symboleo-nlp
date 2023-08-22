from app.classes.spec.domain_object import DomainObject, DomainEvent, Asset, DomainProp
from app.classes.spec.declaration import Declaration, DeclarationType

class IMapDeclarationToDomain:
    def map(self, declaration: Declaration) -> DomainObject:
        raise NotImplementedError()

class DeclarationToDomainMapper(IMapDeclarationToDomain):
    def map(self, declaration: Declaration) -> DomainObject:        
        props = [DomainProp(p.key, p.type) for p in declaration.props]

        if declaration.base_type == DeclarationType.EVENT:
            return DomainEvent(declaration.type, props)
        elif declaration.base_type == DeclarationType.ASSET:
            return Asset(declaration.type, props)
        
        raise NotImplementedError(f'Unhandled domain object type: {declaration.base_type}')