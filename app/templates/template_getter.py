from typing import Dict, List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.contract_updater_config import UpdateConfig

## meat_sale
from app.templates.meat_sale.t_raw.domain_model import get_domain_model as get_meat_sale_raw_dm
from app.templates.meat_sale.t_raw.contract_spec import get_contract_spec as get_meat_sale_raw_cs
from app.templates.meat_sale.t_raw.nl_template import nl_template as meat_sale_raw_nl

from app.templates.meat_sale.t.domain_model import get_domain_model as get_meat_sale_dm
from app.templates.meat_sale.t.contract_spec import get_contract_spec as get_meat_sale_cs
from app.templates.meat_sale.t.nl_template import nl_template as meat_sale_nl

## rental
from app.templates.rental.t.domain_model import get_domain_model as get_rental_t_dm
from app.templates.rental.t.contract_spec import get_contract_spec as get_rental_t_cs
from app.templates.rental.t.nl_template import nl_template as rental_t_nl

from app.templates.rental.t_raw.domain_model import get_domain_model as get_rental_raw_dm
from app.templates.rental.t_raw.contract_spec import get_contract_spec as get_rental_raw_cs
from app.templates.rental.t_raw.nl_template import nl_template as rental_raw_nl

## prop
from app.templates.prop.t.domain_model import get_domain_model as get_prop_t_dm
from app.templates.prop.t.contract_spec import get_contract_spec as get_prop_t_cs
from app.templates.prop.t.nl_template import nl_template as prop_t_nl

from app.templates.prop.t_raw.domain_model import get_domain_model as get_prop_raw_dm
from app.templates.prop.t_raw.contract_spec import get_contract_spec as get_prop_raw_cs
from app.templates.prop.t_raw.nl_template import nl_template as prop_raw_nl

## biomass
from app.templates.biomass.t.domain_model import get_domain_model as get_biomass_t_dm
from app.templates.biomass.t.contract_spec import get_contract_spec as get_biomass_t_cs
from app.templates.biomass.t.nl_template import nl_template as biomass_t_nl

from app.templates.biomass.t_raw.domain_model import get_domain_model as get_biomass_raw_dm
from app.templates.biomass.t_raw.contract_spec import get_contract_spec as get_biomass_raw_cs
from app.templates.biomass.t_raw.nl_template import nl_template as biomass_raw_nl

## indep
from app.templates.indep.t.domain_model import get_domain_model as get_indep_t_dm
from app.templates.indep.t.contract_spec import get_contract_spec as get_indep_t_cs
from app.templates.indep.t.nl_template import nl_template as indep_t_nl

from app.templates.indep.t_raw.domain_model import get_domain_model as get_indep_raw_dm
from app.templates.indep.t_raw.contract_spec import get_contract_spec as get_indep_raw_cs
from app.templates.indep.t_raw.nl_template import nl_template as indep_raw_nl

## energy
from app.templates.energy.t.domain_model import get_domain_model as get_energy_t_dm
from app.templates.energy.t.contract_spec import get_contract_spec as get_energy_t_cs
from app.templates.energy.t.nl_template import nl_template as energy_t_nl

from app.templates.energy.t_raw.domain_model import get_domain_model as get_energy_raw_dm
from app.templates.energy.t_raw.contract_spec import get_contract_spec as get_energy_raw_cs
from app.templates.energy.t_raw.nl_template import nl_template as energy_raw_nl



template_dict: Dict[str, SymboleoContract] = {
    'meat_sale_raw':  SymboleoContract(
        get_meat_sale_raw_dm(),
        get_meat_sale_raw_cs(), 
        meat_sale_raw_nl),
    
    'meat_sale':  SymboleoContract(
        get_meat_sale_dm(),
        get_meat_sale_cs(), 
        meat_sale_nl),
    

    'rental_raw': SymboleoContract(
        get_rental_raw_dm(),
        get_rental_raw_cs(),
        rental_raw_nl
    ),
    
    'rental': SymboleoContract(
        get_rental_t_dm(),
        get_rental_t_cs(),
        rental_t_nl
    ),

    'prop_raw': SymboleoContract(
        get_prop_raw_dm(),
        get_prop_raw_cs(),
        prop_raw_nl
    ),

    'prop': SymboleoContract(
        get_prop_t_dm(),
        get_prop_t_cs(),
        prop_t_nl
    ),

    'biomass_raw': SymboleoContract(
        get_biomass_raw_dm(),
        get_biomass_raw_cs(),
        biomass_raw_nl
    ),

    'biomass': SymboleoContract(
        get_biomass_t_dm(),
        get_biomass_t_cs(),
        biomass_t_nl
    ),

    'indep_raw': SymboleoContract(
        get_indep_raw_dm(),
        get_indep_raw_cs(),
        indep_raw_nl
    ),

    'indep': SymboleoContract(
        get_indep_t_dm(),
        get_indep_t_cs(),
        indep_t_nl
    ),

    'energy_raw': SymboleoContract(
        get_energy_raw_dm(),
        get_energy_raw_cs(),
        energy_raw_nl
    ),

    'energy': SymboleoContract(
        get_energy_t_dm(),
        get_energy_t_cs(),
        energy_t_nl
    ),
}


def get_template(template_str: str) -> SymboleoContract: #pragma: no cover
    if template_str in template_dict:
        return template_dict[template_str]
    else:
        raise ValueError(f'Template {template_str} not found')

