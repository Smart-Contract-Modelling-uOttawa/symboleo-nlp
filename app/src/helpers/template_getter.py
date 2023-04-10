from app.classes.symboleo_contract import SymboleoContract

## SAMPLE (MEAT SALE)
from app.templates.sample.t_raw.sample_domain import get_domain_model as get_sample_raw_dm
from app.templates.sample.t_raw.sample_contract_spec import get_contract_spec as get_sample_raw_cs
from app.templates.sample.t_raw.nl_template import sample_nl_template as sample_raw_nl

from app.templates.sample.t.sample_domain import get_domain_model as get_sample_t_dm
from app.templates.sample.t.sample_contract_spec import get_contract_spec as get_sample_t_cs
from app.templates.sample.t.nl_template import sample_nl_template as sample_t_nl


## RENTAL AGREEMENT
from app.templates.rental_agreement.t.rental_domain import get_domain_model as get_rental_t_dm
from app.templates.rental_agreement.t.rental_contract_spec import get_contract_spec as get_rental_t_cs
from app.templates.rental_agreement.t.nl_template import rental_nl_template as rental_t_nl

from app.templates.rental_agreement.t_raw.rental_domain import get_domain_model as get_rental_raw_dm
from app.templates.rental_agreement.t_raw.rental_contract_spec import get_contract_spec as get_rental_raw_cs
from app.templates.rental_agreement.t_raw.nl_template import rental_nl_template as rental_raw_nl

## PROP MGMT
from app.templates.prop_mgmt.t.domain_model import get_domain_model as get_prop_t_dm
from app.templates.prop_mgmt.t.contract_spec import get_contract_spec as get_prop_t_cs
from app.templates.prop_mgmt.t.nl_template import nl_template as prop_t_nl

from app.templates.prop_mgmt.t_raw.domain_model import get_domain_model as get_prop_raw_dm
from app.templates.prop_mgmt.t_raw.contract_spec import get_contract_spec as get_prop_raw_cs
from app.templates.prop_mgmt.t_raw.nl_template import nl_template as prop_raw_nl

template_dict = {

    # 'meat_sale':  SymboleoContract(
    #     meat_sale_domain_model_template,
    #     meat_sale_contract_spec_template, 
    #     meat_sale_nl_template),
        
    # 'goods_sale':  SymboleoContract(
    #     goods_sale_domain_model_template,
    #     goods_sale_contract_spec_template, 
    #     goods_sale_nl_template),

    'rental_raw': SymboleoContract(
        get_rental_raw_dm(),
        get_rental_raw_cs(),
        rental_raw_nl
    ),

    'rental_t': SymboleoContract(
        get_rental_t_dm(),
        get_rental_t_cs(),
        rental_t_nl
    ),

    'sample_raw': SymboleoContract(
        get_sample_raw_dm(),
        get_sample_raw_cs(),
        sample_raw_nl
    ),

    'sample_t': SymboleoContract(
        get_sample_t_dm(),
        get_sample_t_cs(),
        sample_t_nl
    ),

    'prop_raw': SymboleoContract(
        get_prop_raw_dm(),
        get_prop_raw_cs(),
        prop_raw_nl
    ),

    'prop_t': SymboleoContract(
        get_prop_t_dm(),
        get_prop_t_cs(),
        prop_t_nl
    ),
}


def get_template(template_str): #pragma: no cover
    if template_str in template_dict:
        return template_dict[template_str]
    else:
        raise ValueError(f'Template {template_str} not found')