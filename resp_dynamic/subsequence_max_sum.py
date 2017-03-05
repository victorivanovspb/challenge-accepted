# -*- coding: utf-8 -*-
"""
    Дан массив чисел (числа могут быть как положительными, так и отрицательными).
    Необходимо найти подпоследовательность элементов массива, имеющую максимальную сумму.

    fp = F_PLUS (i):
        сумма определяется как:
            значение текущего элемента
            + максимальное значение: F_PLUS(i+1) или 0
    
    fm = F_MINUS (i):
        сумма определяется как:
            максимальное значение: F_PLUS(i+1) или F_MINUS(i+1)
"""

if __name__ == "__main__":
    mass = [1, 2, -4, 1, 2, 9, -30, 4, 7]
    
    fm = 0
    fp = mass[0]
    f_max = (fp if (fp > fm) else fm)
    for i in mass[1:len(mass)]:
        fm    = (fp if (fp > fm) else fm)
        fp    = (fp if (fp >  0) else  0) + i
        f_max = (fp if (fp > fm) else fm)
    
    print "Subsequence max sum: " + str(f_max)
