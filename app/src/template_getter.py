from app.classes.symboleo_contract import SymboleoContract

from app.templates.meat_sale.symboleo.contract_spec_template import meat_sale_contract_spec_template
from app.templates.meat_sale.symboleo.domain_model_template import meat_sale_domain_model_template
from app.templates.meat_sale.nl_template import nl_template as meat_sale_nl_template

from app.templates.goods_sale.symboleo.contract_spec_template import goods_sale_contract_spec_template
from app.templates.goods_sale.symboleo.domain_model_template import goods_sale_domain_model_template
from app.templates.goods_sale.nl_template import nl_template as goods_sale_nl_template

template_dict = {
    'meat_sale':  SymboleoContract(
        meat_sale_domain_model_template,
        meat_sale_contract_spec_template, 
        meat_sale_nl_template),
    'goods_sale':  SymboleoContract(
        goods_sale_domain_model_template,
        goods_sale_contract_spec_template, 
        goods_sale_nl_template),
}

def get_template(template_str):
    if template_str in template_dict:
        return template_dict[template_str]
    else:
        raise f'Template {template_str} not found'