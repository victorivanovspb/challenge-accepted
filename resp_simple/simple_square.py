# -*- coding: utf-8 -*-
"""
    Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую
    3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
"""
import math

class CalcSquareError(Exception):
    def __init___(self, err):
        super.__init__(self, err)

def calc_square_by_float_side(side_src):
    """Функция, выполняющая расчёт периметра, площади и диагонали квадрата. Выполняется проверка аргумента на тип (float) и значение (больше нуля).
    Ожидаемые исключения (expected exceptions):
        CalcSquareError
        OverflowError
    """
    if type(side_src) is float:
        side = side_src #np.double(side_src)
    else:
        raise CalcSquareError("Source side value must have floating point type.")
    if side <= 0:
        raise CalcSquareError("Source side value must be greather than zero.")
    
    perimeter = side * 4
    area = math.pow(side, 2)
    diag = math.sqrt(math.pow(side, 2) + math.pow(side, 2))
    return (perimeter, area, diag)


if __name__ == "__main__":
    try:
        res = calc_square_by_float_side(10.1)
        print res
    except CalcSquareError, e:
        print e
    
    