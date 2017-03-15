# -*- coding: utf-8 -*-
"""
    Задача 2
        Реализуйте метод, осуществляющий сжатие строки, на основе счётчика
        повторяющихся символов. Например, строка "aabcccccaaa" должна превратиться
        в "a2b1c5a3". Если "сжатая" строка оказывается длиннее исходной, метод должен
        вернуть исходную строку.
"""

def compress_and_get_min(fn):
    def wrapped(source):
        result = fn(source)
        if len(result) > len(source):
            return source
        return result
    return wrapped


@compress_and_get_min
def compress(source):
    result = ""
    counter = 0
    actual_ch = ""
    for idx, ch in enumerate(source):
        if actual_ch == "":
            actual_ch = ch
            counter = 1
        elif actual_ch == ch:
            counter += 1
        elif actual_ch != ch:
            result += actual_ch + str(counter)
            actual_ch = ch
            counter = 1
        
        if idx == len(source) - 1:
            result += actual_ch + str(counter)
        
    return result


def formatter(label, str1, str2, sh = "  "):
    return label + ":\n" + sh + "[" + str1 + "]\n" + sh + "[" + str2 + "]\n"


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    
    s1 = "aabccccccsdddaaa"
    print formatter("s1", s1, compress(s1))

    s2 = "abcdefg"
    print formatter("s2", s2, compress(s2))
    
    s3 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print formatter("s3", s3, compress(s3))
    
    s4 = ".................................."
    print formatter("s4", s4, compress(s4))

    s5 = ""
    print formatter("s5", s5, compress(s5))


