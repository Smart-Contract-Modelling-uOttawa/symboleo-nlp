from app.classes.domain_model.domain_model import Role, Asset, DomainEvent, DomainProp

meat_sale_domain_model = {
    'roles': [
        Role('seller', [
            DomainProp('returnAddress', '', 'str')
        ]),
        Role('buyer', [
            DomainProp('warehouse', '', 'str')
        ])
    ],
    'assets': [
        Asset('perishableGood', None, [
            DomainProp('quantity', '', 'number'),
            DomainProp('quality', '', 'MeatQuality')
        ]),
        Asset('meat', 'perishableGood')
    ],
    'events': [
        DomainEvent('delivered', [
            DomainProp('item', '', 'Meat'),
            DomainProp('deliveryAddress', '', 'str'),
            DomainProp('delDueDate', '', 'date')
        ]),

        DomainEvent('paid', [
            DomainProp('amount', '', 'number'),
            DomainProp('currency', '', 'Currency'),
            DomainProp('from', '', 'Role'),
            DomainProp('to', '', 'Role')
        ]),

        DomainEvent('paidLate', [
            DomainProp('amount', '', 'number'),
            DomainProp('currency', '', 'Currency'),
            DomainProp('from', '', 'Role'),
            DomainProp('to', '', 'Role')
        ])
    ]
}