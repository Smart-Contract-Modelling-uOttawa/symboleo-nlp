from app.classes.symboleo_contract import DomainModel
from app.classes.domain_model.domain_model import Role, Asset, DomainEvent, DomainProp

meat_sale_domain_model_template = DomainModel(
    roles = {
        'seller': Role('seller', [
            DomainProp('address', '123 Main street', 'str')
        ]),
        'buyer': Role('buyer', [
            DomainProp('warehouse', '999 Central Ave', 'str')
        ])
    },
    events = {
        'delivered': DomainEvent('delivered', [
            DomainProp('item', 'meat', 'meat')
        ]),

        'paid': DomainEvent('paid', [
            # DomainProp('amount', '', 'number'),
            # DomainProp('currency', '', 'Currency'),
            DomainProp('from', 'buyer', 'Role'), # Maybe should put the actual buyer/seller objects here...
            DomainProp('to', 'seller', 'Role')
        ]),

        'paidLate': DomainEvent('paidLate', [
            # DomainProp('amount', '', 'number'),
            # DomainProp('currency', '', 'Currency'),
            DomainProp('from', 'buyer', 'Role'),
            DomainProp('to', 'seller', 'Role')
        ]),

        'disclosed': DomainEvent('disclosed', [
        ])
        
    },
    assets = {
        'perishableGood': Asset('perishableGood', None, [
            DomainProp('quantity', '', 'number'),
            DomainProp('quality', '', 'MeatQuality')
        ]),
        'meat': Asset('meat', 'perishableGood')
    }
)
