from app.classes.spec.symboleo_contract import SymboleoContract

class WebContractNL:
    def __init__(self, nl_key:str, nl_text:str):
        self.nl_key = nl_key
        self.nl_text = nl_text

class WebContractSym:
    def __init__(self, contract: SymboleoContract):
        # Domain Objects
        dm = contract.domain_model
        domain_objs = []

        for x in dm.enums:
            next_do = x.to_sym()
            domain_objs.append(next_do)
        
        for x in dm.roles:
            next_do = dm.roles[x].to_sym()
            domain_objs.append(next_do)

        for x in dm.assets:
            next_do = dm.assets[x].to_sym()
            domain_objs.append(next_do)
        
        for x in dm.events:
            next_do = dm.events[x].to_sym()
            domain_objs.append(next_do)
        
        cs = contract.contract_spec
        parms = []
        for x in cs.parameters:
            next_parm = x.to_sym()
            parms.append(next_parm)


        decls = []
        for x in cs.declarations:
            decl = cs.declarations[x].to_sym()
            decls.append(decl)

        obs = []
        for x in cs.obligations:
            ob = cs.obligations[x].to_sym()
            obs.append(ob)
        
        sobs = []
        for x in cs.surviving_obligations:
            sob = cs.surviving_obligations[x].to_sym()
            sobs.append(sob)
        
        pows = []
        for x in cs.powers:
            pow = cs.powers[x].to_sym()
            pows.append(pow)

        self.domain_id = dm.id
        self.id = cs.id
        self.domain_objects = domain_objs
        self.declarations = decls
        self.parameters = parms
        self.obligations = obs
        self.surviving_obligations = sobs
        self.powers = pows


class WebContract:
    def __init__(self, contract: SymboleoContract):
        nl = []
        parms = []
        template_dict = contract.nl_template.template_dict
        
        for nl_key in template_dict:
            template_obj = template_dict[nl_key]
            next_nl = WebContractNL(nl_key, template_obj.str_val)
            nl.append(next_nl)
            for parm_key in template_obj.parameters or []:
                if not template_obj.parameters[parm_key][0].filled:
                    next_parm = f'{nl_key}.{parm_key}'
                    parms.append(next_parm)

        self.nl = nl
        self.parms = parms
        self.sym = WebContractSym(contract)
