# -*- coding: utf-8 -*-
"""
    Задача 2
        Реализуйте метод, осуществляющий сжатие строки, на основе счётчика
        повторяющихся символов. Например, строка "aabcccccaaa" должна превратиться
        в "a2b1c5a3". Если "сжатая" строка оказывается длиннее исходной, метод должен
        вернуть исходную строку.
"""

def compress(source_str):
    n_str = ""
    counter = 0
    glob_counter = 0
    curr = ""
    for ch in source_str:
        if curr == "":
            curr = ch
            counter += 1
        elif curr == ch:
            counter += 1
        elif curr != ch:
            n_str += curr + str(counter)
            curr = ch
            counter = 1
        
        glob_counter += 1
        if glob_counter == len(source_str):
            n_str += curr + str(counter)
            
    return n_str

def formatter(label, str1, str2, sh = "  "):
    return label + ":\n" + sh + str1 + "\n" + sh + str2 + "\n"

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




