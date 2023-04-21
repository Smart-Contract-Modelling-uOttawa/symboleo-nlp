import operator

class SpecHelpers:
    @staticmethod
    def lists_eq(list1:list, list2:list, key):
        if len(list1) != len(list2):
            return False
        
        # Problem is they aren't sorted...
        s1 = sorted(list1, key=operator.attrgetter(key))
        s2 = sorted(list2, key=operator.attrgetter(key))

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        
        return True
