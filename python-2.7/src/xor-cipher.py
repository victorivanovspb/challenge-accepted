# -*- coding: utf-8 -*-
"""
    Простая задачка (https://pythonworld.ru/osnovy/tasks.html)
    XOR-шифрование
    Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать,
    и ключ шифрования, которая возвращает строку, зашифрованную путем применения функции XOR (^)
    над символами строки с ключом. Написать также функцию XOR_uncipher, которая по зашифрованной
    строке и ключу восстанавливает исходную строку.
"""
class KeyIterator(object):
    """Класс-итератор, осуществляющий бесконечную прокрутку символов исходного ключа. Выход по исключению возможен, когда ключ нулевой длины. """
    def __init__(self, key_message):
        self.key = key_message
        if len(self.key) == 0:
            raise StopIteration
        self.pos = 0 
    def __iter__(self):
        return self
    def next(self):
        res = self.key[self.pos]
        self.pos = 0 if len(self.key) - 1 == self.pos else self.pos
        return res      
# END of class KeyIterator ----------------------------------------------------

def xor_cipher(msg, key):
    """Функция шифрования/дешифрования, представляет из себя цикл с двумя итераторами. Выход из цикла по достижении конца сообщения (msg)."""
    res = []
    for char in msg:
        key_val = key.next()
        res.append(char ^ key_val)
    return res

def lines_around(func):
    def wrapped(*args, **kwargs):
        print ""
        func(*args, **kwargs)
    return wrapped

@lines_around
def print_message(msg):
    print msg

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    message = [23,22,11,43,34,54,9,8,3,99,13]
    key = [42,81,27,33,74]

    print_message(message)

    str = xor_cipher(message, KeyIterator(key))
    print_message(str)

    str = xor_cipher(str, KeyIterator(key))
    print_message(str)
