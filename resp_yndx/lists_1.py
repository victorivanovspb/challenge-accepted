# -*- coding: utf-8 -*-
"""
    Есть два списка разной длины. В первом содержатся ключи, а во втором
    значения. Напишите функцию, которая создаёт из этих ключей и значений
    словарь. Если ключу не хватило значения, в словаре должно быть значение
    None. Значения, которым не хватило ключей, нужно игнорировать.  
"""
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class ValuesIterator:
    """Самодельный итератор."""
    def __init__(self, keys, data):
        self.kList = keys
        self.dList = data        
        self.kIndex = 0
        self.dIndex = 0
    def __iter__(self):
        return self
    def next(self):
        if self.kIndex == len(self.kList):
            raise StopIteration
         
        k = self.kList[self.kIndex]
        self.kIndex = self.kIndex + 1
        
        v = self.dList[self.dIndex] if self.dIndex < len(self.dList) else None
        self.dIndex = self.dIndex + 1
            
        return Pair(k, v)


class ValuesIterator2:
    def __init__(self, data):
        self.index = 0
        self.data = data
    def __iter__(self):
        return self
    def next(self):
        if self.index < len(self.data):
            self.index = self.index + 1
            return self.data[self.index - 1]
        else:
            self.index = self.index + 1
            return None


def merge_lists(keys_list, values_list):
    dict = {}
    for k in ValuesIterator(keys_list, values_list):
        dict[k.key] = k.value
    return dict


def merge_lists2(keys_list, values_list):
    dict = {}
    for key, value in zip(keys_list, ValuesIterator2(values_list)):
        dict[key] = value
    return dict

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    keys_list = ['1', '2', '3', '4', '5', '6', '7', '8']
    values_list = [1, 2, 3, 4, 5, 6]
    dict = merge_lists(keys_list, values_list)
    print dict
    dict = merge_lists2(keys_list, values_list)
    print dict
