import copy
from app.classes.symboleo_contract import DomainModel
from app.classes.domain_model.domain_model import DomainProp

# The result of this is a change in the domain model. No change to the contract spec
# Want to convert this to a config that is run by a generic processor
# Maybe an EventProcessor? 
class DeliveryLocationProcessor:
    def __init__(self, nlp, location_extractor):
        self.__nlp = nlp
        self.__location_extractor = location_extractor

    def process(self, value, domain_model: DomainModel) -> DomainModel:
        new_dm = copy.deepcopy(domain_model)
    
        target_event = new_dm.events['delivered']

        delivery_location = self.__location_extractor.extract(value, domain_model)

        new_prop = DomainProp('delivery_location', delivery_location, 'str')
        target_event.props.append(new_prop)

        return new_dm


