from app.classes.symboleo_contract import DomainModel
from app.classes.domain_model.domain_model import Role, Asset, DomainEvent, DomainProp

goods_sale_domain_model_template = DomainModel(
    roles = {
        'seller': Role('seller', []),
        'customer': Role('customer', [])
    },
    events = {
        'sellGoods': DomainEvent('sellGoods', [
            DomainProp('item', 'goods', 'Asset')
        ]),

        'deliverGoods': DomainEvent('deliverGoods', [
            DomainProp('item', 'goods', 'Asset'),
            DomainProp('location', '', 'str')
        ]),

        'provideInvoice': DomainEvent('provideInvoice', []),

        'payInvoice': DomainEvent('payInvoice', [
            # DomainProp('amount', '', 'number'),
            # DomainProp('currency', '', 'Currency'),
        ]),

        'payLate': DomainEvent('payLate', [
            # DomainProp('amount', '', 'number'),
            # DomainProp('currency', '', 'Currency'),
        ]),

        'provideTerminationNotice': DomainEvent('provideTerminationNotice', [])
        
    },
    assets = {
    }
)
