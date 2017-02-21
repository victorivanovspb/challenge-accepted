# -*- coding: utf-8 -*-
"""
    В матрице размерами N * M, состоящей из чисел от 1 до N * M, найдите путь
    из верхнего левого угла в правый нижний угол, двигаясь только вправо и вниз, так,
    чтобы сумма чисел на этом пути минимальна. Учитывайте то, что каждое число в матрице
    встречается лишь единожды.
"""
import random
import itertools

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
    def __init__(self, value, sum):
        self.value = value
        self.sum = sum
    def __repr__(self):
        return "Pair(%r, %r)" % (self.value, self.sum)
    def __str__(self):
        return "(v:%r, s:%r)" % (self.value, self.sum)
    

class Matrix2D(object):
    """
    Горизонталь: ось X с размером columns.  (N, width)
    Вертикаль:   ось Y с размером rows.     (M, height) 
    """
    
    def __init__(self, columns, rows):
        check_int_argument(columns, "matrix width")
        check_int_argument(rows,    "matrix height")
        self.matrix = [[Pair(0, 0) for i in range(rows)] for j in range(columns)]
   
    def width(self):
        return len(self.matrix)
    
    def height(self):
        return len(self.matrix[0])
    
    def __iter__(self):
        self.curr_x = 0
        self.curr_y = 0
        return self
    
    def next(self):
        if self.curr_y >= self.height():
            raise StopIteration
        
        elem = self.matrix[self.curr_x][self.curr_y]
        
        self.curr_x = self.curr_x + 1
        if self.curr_x >= self.width():
            self.curr_x = 0
            self.curr_y = self.curr_y + 1

        return elem


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    n = 10
    m = 5
    matrix = Matrix2D(n, m)
    rand_list = RandomList(1, n * m)

    for elem, rand_val in itertools.izip(matrix, rand_list):
        elem.value = rand_val
        
    for elem in matrix:
        print "%d %d" % (elem.value, elem.sum)
        
    
    