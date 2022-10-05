import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
  
nltk.download('omw-1.4')

class DictSetBuilder:
    def __init__(self):
        self.__lemmatizer = WordNetLemmatizer()

    def build(self, init_dict, pos_c = 'v'):
        dict1 = self._build_dict1(init_dict, pos_c)
        dict2 = self._build_dict2(init_dict)
        dict3 = self._build_dict3(init_dict, pos_c)

        return [
            (dict1, 1),
            (dict2, 0.5),
            (dict3, 0.2)
        ]
        
    def _build_dict1(self, init_dict, pos_c):
        d = dict.fromkeys(init_dict.keys(), [])
        for k in init_dict:
            lemma = self.__lemmatizer.lemmatize(k, pos_c)
            d[k] = [lemma]
        return d
    
    def _build_dict2(self, init_dict):
        d = dict.fromkeys(init_dict.keys(), [])

        for k in init_dict:
            target_ss = init_dict[k]
            d[k] = wn.synset(target_ss).lemma_names()
        return d
    
    def _build_dict3(self, init_dict, pos_c):
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
    



