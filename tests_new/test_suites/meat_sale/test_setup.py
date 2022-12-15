from app.templates.meat_sale.nl_template import nl_template
from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_nlp import TestNLP

from app.src.contract_updater import ContractUpdater
from app.src.processor_lookup import ProcessorLookup


from app.templates.meat_sale.nl_template import parameters as meat_sale_parms

from app.src.rules.contract_spec.predicate_processor import PredicateProcessor
from app.src.rules.domain_model.domain_prop_processor import DomainPropProcessor

from app.src.rules.contract_spec.norm_proposition_updater import NormPropositionUpdater
from app.classes.spec.predicate_function import PredicateFunctionHappens

from app.classes.spec.sym_point import PointAtomContractEvent, ContractEvent
from app.classes.spec.sym_interval import Interval, SituationExpression
from app.classes.spec.sym_situation import ObligationState

from app.src.rules.contract_spec.timeframe.timeframe_extractor_builder import TimeFrameExtractorBuilder
from app.src.rules.contract_spec.condition.condition_extractor_builder import ConditionExtractorBuilder

from app.src.rules.domain_model.amount.amount_extractor_builder import AmountExtractorBuilder
from app.src.rules.domain_model.currency.currency_extractor_builder import CurrencyExtractorBuilder
from app.src.rules.domain_model.location.location_extractor_builder import LocationExtractorBuilder

from app.templates.meat_sale.test_suites.location_extraction import test_suite
from app.templates.meat_sale.symboleo.contract_template import get_template

class MeatSaleTestSetup:
    
    def setup(self) -> ContractUpdater:
        self.nlp = TestNLP.get_nlp()
        self.contract_template = get_template()
        self.norm_updater = NormPropositionUpdater()

        contract_updater = self._get_updater()

        return contract_updater


    def _get_updater(self):
        pdc,pda = self._pd_processor()
        idc,ida = self._id_processor()
        ctf1,ctf2 = self._ctf_processor()

        processor_dict = {
            'DELIVERY_TIMEFRAME': [self._dtf_processor()],
            'DELIVERY_LOCATION': [self._dl_processor()],
            'PAYMENT_DETAILS': [pdc, pda], 
            'PAYMENT_TIMEFRAME': [self._ptf_processor()],
            'INTEREST_DETAILS': [idc, ida],
            'CONFIDENTIALITY_TIMEFRAME': [ctf1, ctf2],
            'DELIVERY_SUSPENSION_CONDITION': [self._dsc_processor()],
            'DELIVERY_RESUMPTION_CONDITION': [self._drc_processor()],
            'TERMINATION_CONDITION': [self._tc_processor()]
        }
        processor_lookup = ProcessorLookup(processor_dict)

        contract_updater = ContractUpdater(processor_lookup)
        return contract_updater

    def _dtf_processor(self):
        delivered_event = self.contract_template.domain_model.events['delivered'].to_obj()
        template = PredicateFunctionHappens(delivered_event)

        default_components = [
            PointAtomContractEvent(ContractEvent('activated'))
        ]
        dtf_extractor = TimeFrameExtractorBuilder.build(self.nlp, template, default_components)

        dtf_pred_proc_config = meat_sale_parms['DELIVERY_TIMEFRAME'][0].config

        dtf_processor = PredicateProcessor(dtf_pred_proc_config, dtf_extractor, self.norm_updater)
        return dtf_processor
    

    def _dl_processor(self):
        dl_extractor = LocationExtractorBuilder.build(self.nlp)

        dl_config = meat_sale_parms['DELIVERY_LOCATION'][0].config

        dl_processor = DomainPropProcessor(dl_config, dl_extractor)
        return dl_processor
    

    def _pd_processor(self):
        pd_currency_extractor = CurrencyExtractorBuilder.build(self.nlp)

        pd_curr_config = meat_sale_parms['PAYMENT_DETAILS'][1].config

        pd_curr_processor = DomainPropProcessor(pd_curr_config, pd_currency_extractor)

        pd_amount_extractor = AmountExtractorBuilder.build(self.nlp)

        pd_amt_config = meat_sale_parms['PAYMENT_DETAILS'][0].config

        pd_amt_processor = DomainPropProcessor(pd_amt_config, pd_amount_extractor)

        return pd_curr_processor, pd_amt_processor
    

    def _ptf_processor(self):
        paid_event = self.contract_template.domain_model.events['paid'].to_obj()
        paid_template = PredicateFunctionHappens(paid_event)
        default_components = [
            PointAtomContractEvent(ContractEvent('activated'))
        ]
        ptf_extractor = TimeFrameExtractorBuilder.build(self.nlp, paid_template, default_components)

        ptf_config = meat_sale_parms['PAYMENT_TIMEFRAME'][0].config

        ptf_processor = PredicateProcessor(ptf_config, ptf_extractor, self.norm_updater)
        
        return ptf_processor    


    def _id_processor(self):
        id_currency_extractor = CurrencyExtractorBuilder.build(self.nlp)

        id_curr_config = meat_sale_parms['INTEREST_DETAILS'][1].config

        id_curr_processor = DomainPropProcessor(id_curr_config, id_currency_extractor)

        id_amount_extractor = AmountExtractorBuilder.build(self.nlp)

        id_amt_config = meat_sale_parms['INTEREST_DETAILS'][0].config

        id_amt_processor = DomainPropProcessor(id_amt_config, id_amount_extractor)

        return id_curr_processor, id_amt_processor


    def _ctf_processor(self):
        disclosed_event = self.contract_template.domain_model.events['disclosed'].to_obj()
        disclosed_template = PredicateFunctionHappens(disclosed_event)

        ctf_extractor = TimeFrameExtractorBuilder.build(self.nlp, disclosed_template)

        ctf_config1 = meat_sale_parms['CONFIDENTIALITY_TIMEFRAME'][0].config

        ctf_processor1 = PredicateProcessor(ctf_config1, ctf_extractor, self.norm_updater)

        ctf_config2 = meat_sale_parms['CONFIDENTIALITY_TIMEFRAME'][1].config

        ctf_processor2 = PredicateProcessor(ctf_config2, ctf_extractor, self.norm_updater)
    
        return ctf_processor1, ctf_processor2
    
    def _dsc_processor(self):
        suspension_template = None
        sc_extractor = ConditionExtractorBuilder.build(self.nlp, suspension_template)

        sc_config = meat_sale_parms['DELIVERY_SUSPENSION_CONDITION'][0].config

        sc_processor = PredicateProcessor(sc_config, sc_extractor, self.norm_updater)

        return sc_processor
    

    def _drc_processor(self):

        resumption_template = None
        default_components = [
            Interval(SituationExpression(ObligationState('Suspension', 'delivery')))
        ]
        rc_extractor = ConditionExtractorBuilder.build(self.nlp, resumption_template, default_components)

        rc_config = meat_sale_parms['DELIVERY_RESUMPTION_CONDITION'][0].config

        drc_processor = PredicateProcessor(rc_config, rc_extractor, self.norm_updater)

        return drc_processor
    

    def _tc_processor(self):
        termination_template = None
        default_components = [
            ObligationState('Violation', 'delivery')
        ]
        tc_extractor = ConditionExtractorBuilder.build(self.nlp, termination_template, default_components)

        tc_config = meat_sale_parms['TERMINATION_CONDITION'][0].config

        tc_processor = PredicateProcessor(tc_config, tc_extractor, self.norm_updater)
        return tc_processor