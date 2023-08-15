from app.src.custom_event_extractor.nlp.doc_parser import IParseDoc, NlpDoc, DocUnit

class FakeDocParser(IParseDoc):
    def __init__(self):
        self.__fake_dict = {
            'apple pie': NlpDoc([
                DocUnit('apple', 'NN', 'compound', 'pie'),
                DocUnit('pie', 'NN', 'ROOT', 'pie'),
            ]),

            'all project components': NlpDoc([
                DocUnit('all', 'DT', 'det', 'components'),
                DocUnit('project', 'NN', 'compound', 'components'),
                DocUnit('components', 'NNS', 'ROOT', 'components'),
            ]),

            'the party': NlpDoc([
                DocUnit('the', 'DT', 'det', 'party'),
                DocUnit('party', 'NN', 'ROOT', 'party'),
            ]),
            
            'invoice receipt': NlpDoc([
                DocUnit('invoice', 'NN', 'compound', 'receipt'),
                DocUnit('receipt', 'NN', 'ROOT', 'receipt'),
            ]),

            'any product': NlpDoc([
                DocUnit('any', 'DT', 'det', 'product'),
                DocUnit('product', 'NN', 'ROOT', 'product'),
            ]),

            'the original digital photo files': NlpDoc([
                DocUnit('the', 'DT', 'det', 'files'),
                DocUnit('original', 'JJ', 'amod', 'files'),
                DocUnit('digital', 'JJ', 'amod', 'photo'),
                DocUnit('photo', 'NN', 'compound', 'files'),
                DocUnit('files', 'NNS', 'ROOT', 'files'),
            ]),

            'authorization': NlpDoc([
                DocUnit('authorization', 'NN', 'ROOT', 'authorization'),
            ]),

            'productivity': NlpDoc([
                DocUnit('productivity', 'NN', 'ROOT', 'productivity'),
            ]),

            'disclosure': NlpDoc([
                DocUnit('disclosure', 'NN', 'ROOT', 'disclosure'),
            ]),

            'services': NlpDoc([
                DocUnit('services', 'NNS', 'ROOT', 'services')
            ]),

            'approval': NlpDoc([
                DocUnit('approval', 'NN', 'ROOT', 'approval')
            ]),

            'security deposit': NlpDoc([
                DocUnit('security', 'NN', 'compound', 'deposit'),
                DocUnit('deposit', 'NN', 'ROOT', 'deposit'),
            ]),

            # Roles
            'partyA': NlpDoc([DocUnit('partyA', 'NN', 'ROOT', 'partyA')]),
            'distributor': NlpDoc([DocUnit('distributor', 'NN', 'ROOT', 'distributor')]),
            'cisco': NlpDoc([DocUnit('cisco', 'NN', 'ROOT', 'cisco')]),
            'Porex': NlpDoc([DocUnit('Porex', 'NN', 'ROOT', 'Porex')]),
            'Cerus': NlpDoc([DocUnit('Cerus', 'NN', 'ROOT', 'Cerus')]),
            'Prime': NlpDoc([DocUnit('Prime', 'NN', 'ROOT', 'Prime')]),
            'Dolphin': NlpDoc([DocUnit('Dolphin', 'NN', 'ROOT', 'Dolphin')]),

            'renter': NlpDoc([DocUnit('renter', 'NN', 'ROOT', 'renter')]),
            'buyer': NlpDoc([DocUnit('buyer', 'NN', 'ROOT', 'buyer')]),
            'GridIron': NlpDoc([DocUnit('GridIron', 'NN', 'ROOT', 'GridIron')]),
            'Shi Farms': NlpDoc([DocUnit('Shi Farms', 'NN', 'ROOT', 'Shi Farms')]),

            # Full stack tests
            'payment': NlpDoc([
                DocUnit('payment', 'NN', 'ROOT', 'payment'),
            ]),
            'third-party analysis': NlpDoc([
                DocUnit('third-party', 'JJ', 'amod', 'analysis'),
                DocUnit('analysis', 'NN', 'ROOT', 'analysis')
            ]),
            'biomass': NlpDoc([
                DocUnit('biomass', 'NN', 'ROOT', 'biomass')
            ]),
        }

    def parse(self, str_val: str) -> NlpDoc:
        if str_val in self.__fake_dict:
            return self.__fake_dict[str_val]
        
        print(f'{str_val} not found in fake_doc_parser...')

        return NlpDoc([
            DocUnit(x, self._check_plural(x), 'ROOT', x) for x in str_val.split(' ')
        ])
        

    def _check_plural(self, t):
        if t[-1] == 's':
            return 'NNS'
        else:
            return 'NN'