import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

from app.src.primitive_identifiers.dicts.init_event_dicts import EventDictValue, init_event_dicts

nltk.download('omw-1.4')

class EventDictSetBuilder:
    def __init__(self):
        self.__lemmatizer = WordNetLemmatizer()

    @staticmethod
    def build_all():
        builder = EventDictSetBuilder()
        all_sets = {}

        for k in ['obligation', 'power', 'contract']:
            all_sets[k] = builder.build_event_dicts(init_event_dicts[k])

        return all_sets


    def build_event_dicts(self, init_dict: dict[str, EventDictValue], pos_c = 'v'):
        single_lemma_dict = self._build_single_lemma_dict(init_dict, pos_c)
        custom_list_dict = self._build_custom_list_dict(init_dict)
        synset_lemma_dict = self._build_synset_lemma_dict(init_dict)
        extended_lemma_dict = self._build_extended_lemma_dict(init_dict, pos_c)

        return [
            (single_lemma_dict, 1),
            (custom_list_dict, 0.75),
            (synset_lemma_dict, 0.5),
            (extended_lemma_dict, 0.25)
        ]
        
    def _build_single_lemma_dict(self, init_dict: dict[str, EventDictValue], pos_c):
        d = dict.fromkeys(init_dict.keys(), [])
        for k in init_dict:
            lemma = self.__lemmatizer.lemmatize(k, pos_c)
            d[k] = [lemma]
        return d
    

    def _build_custom_list_dict(self, init_dict: dict[str, EventDictValue]):
        d = dict.fromkeys(init_dict.keys(), [])
        for k in init_dict:
            d[k] = init_dict[k].custom_list
        return d
    

    def _build_synset_lemma_dict(self, init_dict: dict[str, EventDictValue]):
        d = dict.fromkeys(init_dict.keys(), [])

        for k in init_dict:
            target_ss = init_dict[k].synset_name
            d[k] = wn.synset(target_ss).lemma_names()
        return d
    

    def _build_extended_lemma_dict(self, init_dict, pos_c):
        d = dict.fromkeys(init_dict.keys(), [])
        for k in init_dict:
            lemma = self.__lemmatizer.lemmatize(k, pos_c)

            synsets = wn.synsets(lemma)
            dict_list = []

            for ss in synsets:
                if (ss.pos() != pos_c):
                    continue

                next_lemmas = ss.lemma_names()
                dict_list.extend(next_lemmas)

            d[k] = list(set(dict_list))
        
        return d
    



