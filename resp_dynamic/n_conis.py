# -*- coding: utf-8 -*-
"""
    Необходимо определить минимальное количество монет, необходимых для возрата суммы N.
    Доступны только монеты достоинством: 1, 2, 3 и 5.
    
    Поиск минимального значения осуществляется рекурсивным вызовом целевой функции.
"""
import sys
sys.setrecursionlimit(1500)

class NcoinsError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


class Ncoins(object):
    def __init__(self, coins):
        if type(coins) is tuple:
            self.coins = coins
        else:
            raise TypeError("argument is not a tuple")

    def func(self, n):
        """Целевая функция"""
        min_val = -1
        if n > 0:
            for coin in coins:
                val = n - coin
                if val == 0:
                    min_val = val
                    break
                elif val > 0:
                    res = self.func(val)
                    if min_val == -1 or res < min_val:
                        min_val = res
                else:
                    continue
            if min_val == -1:
                raise NcoinsError("cannot get any result")
            min_val = min_val + 1
        elif n == 0:
            min_val = 0
        else:
            raise ValueError("argument value can not be less than zero")
        return min_val


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    n = 15
    coins = (1, 2, 3, 5)
    try:
        res = Ncoins(coins).func(n)
    except (NcoinsError, ValueError, TypeError), e:
        print e
    else:
        print "Result: %d" % (res)
