# -*- coding: utf-8 -*
import sys
import numpy

def parse_integers(msg):
    result = list()
    mass = msg.split(" ")
    for i in mass:
        result.append(int(i))
    return result

class Diagonal(object):
    """Итератор, с помощью которого осуществляется проход по всем точкам конкретной диагонали, заданной координатами её начала: i и j."""
    def __init__(self, n, m, i, j):
        self.n = n
        self.m = m
        self.start_i = i
        self.start_j = j
    
    def dprint(self):
        print str(self.start_i) + " " + str(self.start_j)
    
    def __iter__(self):
        self.stop = False
        self.i = self.start_i
        self.j = self.start_j
        return self
    
    def next(self):
        if self.stop:
            raise StopIteration
        result = (self.i, self.j)
        if self.i - 1 <= 0 or self.j + 1 > self.m:
            self.stop = True
        else:
            self.i -= 1
            self.j += 1
        return result

class DiagonalLines(object):
    """Итератор, с помощью которого осуществляется проход по всем диагоналям, перпендикулярным пути вдоль основной диагонали: от (1,1) до (n,m)."""
    def __init__(self, n, m):
        if n < 1 or m < 1:
            raise ValueError("class DiagonalLines: 'n' or 'm' values cannot be less than 1")
        self.n = n
        self.m = m
    
    def __iter__(self):
        self.stop = False
        self.i = 1
        self.j = 1
        return self
    
    def next(self):
        if self.stop:
            raise StopIteration
        result = Diagonal(self.n, self.m, self.i, self.j)
        if self.i < self.n:
            self.i += 1
        elif self.j < self.m:
            self.j += 1
        else:
            self.stop = True
        return result    

if __name__ == "__main__":
    #number_of_tests = int(sys.stdin.readline())
    #for t in xrange(number_of_tests):
    print "Enter 'n':" #sys.stdout.write("Enter 'n': ")
    n = int(sys.stdin.readline())

    print "Enter 'm':" #sys.stdout.write("Enter 'm': ")
    m = int(sys.stdin.readline())
    #nm = parse_integers(sys.stdin.readline().strip("\n"))
    #n = nm[0]
    #m = nm[1]
    vip = n * m # значение важности персоны (см. условия задачи).
    matrix = numpy.matrix(numpy.zeros((n, m)))
    for current_diagonal in DiagonalLines(n, m):
        for pos in current_diagonal:
            matrix[pos[0] - 1, pos[1] - 1] = vip # корректировка: индексация в numpy идёт от нуля
            vip -= 1
        
    print matrix
 
    
    