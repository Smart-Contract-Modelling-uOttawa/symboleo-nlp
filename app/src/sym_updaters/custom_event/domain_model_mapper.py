from app.classes.spec.domain_object import DomainObject, DomainEvent, Asset, DomainProp
from app.classes.spec.declaration import Declaration

class IMapDeclarationToDomain:
    def map(self, declaration: Declaration) -> DomainObject:
        raise NotImplementedError()

# TODO: Create a template for the domainEvent... so that we can create new ones
class DeclarationToDomainMapper(IMapDeclarationToDomain):
    def map(self, declaration: Declaration) -> DomainObject:        
        props = [DomainProp(p.key, p.type) for p in declaration.props]

        if declaration.base_type == 'events':
            return DomainEvent(declaration.type, props)
        elif declaration.base_type == 'assets':
            return Asset(declaration.type, props)
        
        raise NotImplementedError(f'Unhandled domain object type: {declaration.base_type}')