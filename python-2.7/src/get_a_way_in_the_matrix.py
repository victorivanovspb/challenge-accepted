# -*- coding: utf-8 -*-
"""
    В матрице размерами N * M, состоящей из чисел от 1 до N * M, найдите путь
    из верхнего левого угла в правый нижний угол, двигаясь только вправо и вниз, так,
    чтобы сумма чисел на этом пути минимальна. Учитывайте то, что каждое число в матрице
    встречается лишь единожды.
"""
import random
import numpy

def check_int_argument(arg, arg_name):
    if not isinstance(arg, int):
        raise TypeError("type of '" + arg_name + "' argument is not integer: " + str(type(arg)))


class RandomList(object):
    def __init__(self, min_value, max_value):
        check_int_argument(min_value, "min")
        check_int_argument(max_value, "max")
        if min_value >= max_value:
            raise ValueError("'min' value cannot be greather (or equal) than 'max' value.")
        self.min_value = min_value
        self.max_value = max_value
        
    def __iter__(self):
        self.numbers = list()
        for i in xrange(self.min_value, self.max_value + 1):
            self.numbers.append(i)
        return self
    
    def next(self):
        if len(self.numbers) == 0:
            raise StopIteration
        i = random.randrange(0, len(self.numbers))
        return self.numbers.pop(i)


class Matrix(object):
    def __init__(self, width, height):
        check_int_argument(width, "matrix width")
        check_int_argument(height, "matrix height")
        self.matrix = numpy.zeros((width, height)).astype(int)
        
    def print_matrix(self):
        print self.matrix


class RandMatrix(Matrix):
    def __init__(self, width, height):
        super(RandMatrix, self).__init__(width, height)
        rand_list = RandomList(1, width * height)
        it = numpy.nditer(self.matrix, flags=['multi_index'])
        for r in rand_list:
            if it.finished:
                break
            #print "it_val=%d it_coords=<%s> rand_val=%d" % (it[0], it.multi_index, r)
            self.matrix[it.multi_index[0]][it.multi_index[1]] = r
            it.iternext()


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    m = RandMatrix(10, 10)
    m.print_matrix()
    #rlist = RandomList(1, 100)
    #res = list()
    #for elem in rlist:
    #    res.append(elem)
    #print res

    #n, m = 10, 10
    #matrix = numpy.zeros((n, m)).astype(int)
    
    #print matrix[2, 3]
    #matrix[2, 3] = 4
    #print matrix
    
     
