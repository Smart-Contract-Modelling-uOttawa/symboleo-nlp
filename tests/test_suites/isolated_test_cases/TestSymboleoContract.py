from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract, SymboleoContract
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.declaration import Declaration
from app.classes.spec.norm import Obligation
from app.classes.spec.nl_template import NLTemplate, TemplateObj

from app.classes.operations.user_input import UserInput, UnitType

from app.src.update_processor.domain_model_mapper import IMapDeclarationToDomain

from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode


class TestCase:
    def __init__(
        self,
        case_id: str,
        init_sym: SymboleoContract,
        op_code: OpCode,
        update_config: UpdateConfig,
        exp_sym: SymboleoContract = None
    ):
        self.case_id = case_id
        self.init_sym = init_sym
        self.op_code = op_code
        self.update_config = update_config
        self.exp_sym = exp_sym

class TestInfo:
    def __init__(
        self,
        full_nl: str,
        refinement: str, 
        declarations: List[Declaration],
        obligation: Obligation
    ):
        self.full_nl = full_nl
        self.declarations = declarations
        self.obligation = obligation

class TestSymboleoContractMaker:
    # def __init__(
    #         self,
    #         declarations,
    #         obligations
    #         ):
    #     self.declarations = 

    def __init__(self, declarationToDomainMapper: IMapDeclarationToDomain):
        self.__mapper = declarationToDomainMapper

    def make_contract(self, test_info: TestInfo) -> SymboleoContract:
        # Build the domain model
        roles = {}
        assets = {}
        events = {}
        for x in test_info.declarations:
            next_dm = self.__mapper.map(x)
            if next_dm.base_type_name == 'roles':
                roles[next_dm.name] = next_dm
            elif next_dm.base_type_name == 'assets':
                assets[next_dm.name] = next_dm
            elif next_dm.base_type_name == 'events':
                events[next_dm.name] = next_dm

        domain_model = DomainModel('domain_model', roles, [], events, assets)

        # Build contract spec
        ob_id = test_info.obligation.id
        obligations = {
            ob_id: test_info.obligation
        }
        declarations = {
            x.name: x for x in test_info.declarations
        }

        contract_spec = ContractSpec(
            'test',
            [], #Parms?
            declarations,
            [],
            [],
            obligations,
            {},
            {},
            [])
        
        # Build template
        nl_template = NLTemplate({
            'sample': TemplateObj(test_info.nl, {
                # TODO: Parm config
            })
        })

        return SymboleoContract(
            domain_model,
            contract_spec,
            nl_template
        )