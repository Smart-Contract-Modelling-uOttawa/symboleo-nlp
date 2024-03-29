
from app.classes.operations.dependencies import Dependencies

from app.src.domain_update_extractor.domain_update_extractor import DomainUpdateExtractor
from app.src.domain_update_extractor.asset_declaration_extractor import AssetDeclarationExtractor
from app.src.domain_update_extractor.declaration_mapper import DeclarationMapper
from app.src.domain_update_extractor.asset_declaration_mapper import AssetDeclarationMapper
from app.src.domain_update_extractor.event_declaration_mapper import EventDeclarationMapper
from app.src.domain_update_extractor.declaration_prop_mapper import DeclarationPropMapper
from app.src.domain_update_extractor.domain_model_mapper import DeclarationToDomainMapper
from app.src.domain_update_extractor.contract_parm_mapper import ContractParmMapper
from app.src.object_mappers.date_mapper import DateMapper

class DomainUpdateExtractorBuilder:

    @staticmethod
    def build(deps: Dependencies):
        asset_extractor = AssetDeclarationExtractor()
        asset_decl_mapper = AssetDeclarationMapper(asset_extractor)

        prop_mapper = DeclarationPropMapper()
        event_decl_mapper = EventDeclarationMapper(prop_mapper)

        decl_mapper = DeclarationMapper(
            asset_decl_mapper,
            event_decl_mapper
        )

        domain_mapper = DeclarationToDomainMapper()

        date_mapper = DateMapper()
        contract_parm_extractor = ContractParmMapper(date_mapper)

        return DomainUpdateExtractor(
            decl_mapper,
            domain_mapper,
            contract_parm_extractor
        )