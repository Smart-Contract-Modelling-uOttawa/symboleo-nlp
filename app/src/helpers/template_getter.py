from app.classes.symboleo_contract import SymboleoContract

#from app.templates.meat_sale.symboleo.contract_spec_template import meat_sale_contract_spec_template
#from app.templates.meat_sale.symboleo.domain_model_template import meat_sale_domain_model_template
#from app.templates.meat_sale.nl_template import nl_template as meat_sale_nl_template

#from app.templates.goods_sale.symboleo.contract_spec_template import goods_sale_contract_spec_template
#from app.templates.goods_sale.symboleo.domain_model_template import goods_sale_domain_model_template
#from app.templates.goods_sale.nl_template import nl_template as goods_sale_nl_template

from app.templates.sample.t_raw.sample_domain import get_domain_model as get_sample_raw_dm
from app.templates.sample.t_raw.sample_contract_spec import get_contract_spec as get_sample_raw_cs
#from app.templates.sample.t_raw.nl_template import nl_template as sample_raw_nl

from app.templates.sample.t.sample_domain import get_domain_model as get_sample_t_dm
from app.templates.sample.t.sample_contract_spec import get_contract_spec as get_sample_t_cs
from app.templates.sample.t.nl_template import sample_nl_template as sample_t_nl

template_dict = {

    # 'meat_sale':  SymboleoContract(
    #     meat_sale_domain_model_template,
    #     meat_sale_contract_spec_template, 
    #     meat_sale_nl_template),
        
    # 'goods_sale':  SymboleoContract(
    #     goods_sale_domain_model_template,
    #     goods_sale_contract_spec_template, 
    #     goods_sale_nl_template),

    'sample_raw': SymboleoContract(
        get_sample_raw_dm(),
        get_sample_raw_cs(),
        None
        #sample_raw_nl
    ),

    'sample_t': SymboleoContract(
        get_sample_t_dm(),
        get_sample_t_cs(),
        sample_t_nl
    ),
}

def get_template(template_str):
    if template_str in template_dict:
        return template_dict[template_str]
    else:
        raise f'Template {template_str} not found'