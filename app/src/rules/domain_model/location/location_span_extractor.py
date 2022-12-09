class IExractLocationSpans:
    def extract(self, doc):
        raise NotImplementedError()

class LocationSpanExtractor(IExractLocationSpans):
    def extract(self, doc):
        result = None
        for nc in list(doc.noun_chunks):
            if not result or len(nc.text) > len(result.text):
                result = nc
        
        return result

    