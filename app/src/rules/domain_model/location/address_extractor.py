import address_parser
import ez_address_parser

class IExtractAddresses:
    def extract(self, doc):
        raise NotImplementedError()

class AddressExtractor(IExtractAddresses):
    # Country code: US, CAN
    def __init__(self, country_code='US'):
        self.__country_code = country_code
    
    def extract(self, doc):
        #TODO: add in separate parsers for us and ca

        results = []

        # Define some patterns...

        return results
        