# -*- coding: utf-8 -*-
"""
    В матрице размерами N * M, состоящей из чисел от 1 до N * M, найдите путь
    из верхнего левого угла в правый нижний угол, двигаясь только вправо и вниз, так,
    чтобы сумма чисел на этом пути минимальна. Учитывайте то, что каждое число в матрице
    встречается лишь единожды.
"""
import random
import numpy
import copy

def check_int_argument(arg, arg_name):
    if not isinstance(arg, int):
        raise TypeError("type of '" + arg_name + "' argument is not integer: " + str(type(arg)))


class RandomList(object):
    """Набор чисел в диапазоне [min_value, max_value], расположенных в случайном порядке.
    Произвольность расположения чисел обеспечивается в методе итератора next(): randrange(начало списка, размер списка),
    после чего элемент с указанным индексом удаляется из списка."""
    
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

class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Pair(%r, %r)" % (self.x, self.y)
    def __str__(self):
        return "(%r, %r)" % (self.x, self.y)
    

class Coordinate(Pair):
    def __init__(self, x, y):
        check_int_argument(x, "x")
        check_int_argument(y, "y")
        if x < 0:
            raise ValueError("'x' coordinate cannot be less than zero.")
        super(Coordinate, self).__init__(x, y)
        
    def step(self):
        self.x = self.x + 1
        self.y = self.y + 1


class Matrix2D(object):
    """Простая двумерная матрица с итератором IterDiagonal по главной диагонали (от левого угла сверху до правого угла снизу).
    Итератор выдает два объекта, каждый из которых представляет собой итератор: IterHorizontal, двигающийся вправо по ячейкам текущей
    горизонтальной линии в матрице; а также IterVertical, двигающийся вниз по ячейкам текущей вертикальной линии в матрице.
    
    Горизонталь: ось X с размером width.
    Вертикаль:   ось Y с размером height. 
    """
    
    def __init__(self, width, height):
        check_int_argument(width, "matrix width")
        check_int_argument(height, "matrix height")
        self.matrix = numpy.zeros((width, height)).astype(int)
        
        #print "x=%d, y=%d" % (self.width(), self.height())
    
    def width(self):
        return self.matrix.shape[1]
    
    def height(self):
        return self.matrix.shape[0]
    
    def print_matrix(self):
        print self.matrix
    
    def __iter__(self):
        self.pointer = Coordinate(0, 0)
        return self
    
    def next(self):
        if self.pointer.x >= self.width():
            raise StopIteration
        if self.pointer.y >= self.height():
            raise StopIteration
        
        
        self.pointer.step()
        #self.coord['x']


class RandMatrix2D(Matrix2D):
    def __init__(self, width, height):
        super(RandMatrix2D, self).__init__(width, height)
        rand_list = RandomList(1, width * height)
        it = numpy.nditer(self.matrix, flags=['multi_index'])
        for r in rand_list:
            if it.finished:
                break
            #print "it_val=%d it_coords=<%s> rand_val=%d" % (it[0], it.multi_index, r)
            self.matrix[it.multi_index[0]][it.multi_index[1]] = r
            it.iternext()


class SublineMatrix2D(object):
    def __init__(self, matrix, xy_coord):
        self.matrix = matrix
        self.xy_origin = xy_coord
        self.xy_current = copy.copy(self.xy_origin)
    
    def __iter__(self):
        self.xy_current.x = self.xy_origin.x
        self.xy_current.y = self.xy_origin.y
        return self
    
    def next(self):
        raise StopIteration # Without orientation (in subclasses: vertical, horizontal...) iterator doen't move.

    def get_min_sum(self):
        if self.xy_current.x > 0:
            _left = self.matrix[self.xy_current.x - 1][self.xy_current.y]
            
        pass
        # get_near
        # get_prev

    def get_current_x(self):
        return self.xy_current.x
    
    def get_current_y(self):
        return self.xy_current.y


class VerticalSublineMatrix2D(SublineMatrix2D):

    def __init__(self, matrix, xy_coordinate):
        super(VerticalSublineMatrix2D, self).__init__(matrix, xy_coordinate)
        pass
    
    def __iter__(self):
        return self

    def next(self):
        raise StopIteration

    def get_min_sum(self):
        pass
        # get_near
        # get_prev


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    m = RandMatrix2D(10, 5)
    m.print_matrix()
    
    p = Pair('a3',10)
    print p
    
    c = Coordinate(1, 1)
    print c.x
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
    
     
