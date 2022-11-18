class IExtractAddresses:
    def extract(self, doc):
        raise NotImplementedError()

class AddressExtractor(IExtractAddresses):
    def __init__(self):
        self.s = 0
    
    def extract(self, doc):
        results = []

        # Define some patterns...

        return results
        