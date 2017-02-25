# -*- coding: utf-8 -*-
"""
    Перед нами сто дверей (с номерами от 1 до 100).
    Изначально все двери закрыты.
    Последовательно выполяется 100 шагов: 
    1. Меняется текущее состояние у всех дверей (у каждой первой).
    2. Меняется текущее состояние у каждой второй.
    3. ...у каждой третьей.
    ...
    100. Меняется текущее состояние только у сотой двери.
    Необходимо найти открытые двери.
"""
class Door(object):
    @staticmethod
    def is_closed():
        return False
    
    def __init__(self, is_open = True):
        if type(is_open) is not bool:
            raise TypeError("type of argument is not a boolean")
        self.is_open = is_open
    
    def invert(self):
        self.is_open = False if self.is_open else True
    
    def __str__(self):
        return "open" if self.is_open else "closed"
    
    def __repr__(self):
        return "O" if self.is_open else "X"


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    doors = [Door(Door.is_closed()) for i in range(100)]
    print doors
    for i in xrange(1, 101):
        for idx, current in enumerate(doors):
            idx = idx + 1
            if idx % i == 0:
                current.invert()
    print doors

    counter = 0
    for idx, current in enumerate(doors):
        if current.is_open:
            counter = counter + 1
            print "Дверь №%d открыта" % (idx + 1)
    print "Всего открытых дверей: %d" % (counter)
