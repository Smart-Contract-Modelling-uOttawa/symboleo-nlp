from app.classes.symboleo_contract import SymboleoContract

from app.templates.meat_sale.contract_spec_template import meat_sale_contract_spec_template as contract_spec
from app.templates.meat_sale.domain_model_template import meat_sale_domain_model_template as domain_model
from app.templates.meat_sale.nl_template import nl_template


def get_template():
    return SymboleoContract(domain_model, contract_spec, nl_template)