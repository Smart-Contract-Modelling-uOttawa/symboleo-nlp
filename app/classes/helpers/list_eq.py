import operator

class ClassHelpers:
    @staticmethod
    def lists_eq(list1:list, list2:list, key):
        if len(list1) != len(list2):
            return False
        
        s1 = sorted(list1, key=operator.attrgetter(key))
        s2 = sorted(list2, key=operator.attrgetter(key))
        
        # for s in s1:
        #     print('1')
        #     s.print_me()

        # for s in s2:
        #     print('2')
        #     s.print_me()

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        
        return True

    @staticmethod
    def simple_lists_eq(list1:list, list2:list):
        if not list1 and not list2:
            return True
        
        if len(list1) != len(list2):
            return False
        
        s1 = sorted(list1)
        s2 = sorted(list2)

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        
        return True


    def dicts_eq(dict1:dict, dict2:dict) -> bool:
        k1 = sorted(list(dict1.keys()))
        k2 = sorted(list(dict2.keys()))

        if not ClassHelpers.simple_lists_eq(k1, k2):
            return False

        for x in dict1:
            if dict1[x] != dict2[x]:
                return False
        
        return True