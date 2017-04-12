#*.* coding: utf-8 *.*
"""
    Необходимо перевернуть строку различными способами.
"""
def get_strings_original_and_result(func_to_decorate):
    """Декоратор, конкатенирующий строки: исходную и результат."""
    def wrapper(*args, **kwargs):
        result = list()
        result.append(args[0])
        result.append(func_to_decorate(*args, **kwargs))
        return " ".join(result)
    return wrapper

@get_strings_original_and_result
def reverse_v1(orig):
    """Переворот строки (вариант №1): стандартно."""
    return orig[::-1] if type(orig) is str else ""

@get_strings_original_and_result
def reverse_v2(orig):
    """Переворот строки (вариант №2): посимвольно с конца к началу."""
    result = list()
    if type(orig) is str:
        i = len(orig) - 1 # last element
        while i >= 0:
            result.append(orig[i])
            i -= 1
    return "".join(result)

def substr_first_go_back(m):
    """Первый элемент передаваемой подстроки ставится в самый конец, а для подстроки со 2-го элемента до конца вызывается эта же функция."""
    if len(m) > 0:
        return substr_first_go_back(m[1:]) + m[0]
    return ""

@get_strings_original_and_result
def reverse_v3(orig):
    """Переворот строки (вариант №3): рекрсивный вызов целевой функции 'substr_first_go_back'."""
    return substr_first_go_back(orig) if type(orig) is str else ""

@get_strings_original_and_result
def reverse_v4(orig):
    """Переворот строки (вариант №4): вызов 'reversed'.""" 
    return "".join(reversed(orig)) if type(orig) is str else ""
    

@get_strings_original_and_result
def reverse_v5(orig):
    """Переворот строки (вариант №5): получения итератора от вызова 'reversed' и работа в цикле.""" 
    result = list()
    if type(orig) is str:
        for i in reversed(orig):
            result.append(i)
    return "".join(result)

@get_strings_original_and_result
def reverse_v6(orig):
    """Переворот строки (вариант №6): проход по строке в цикле от края до середины с заменой текущих крайних элементов.""" 
    result = ""
    if type(orig) is str:
        m = list(orig)
        beg = 0
        end = len(m) - 1
        while beg < end:
            tmp = m[beg]
            m[beg] = m[end]
            m[end] = tmp
            beg += 1
            end -= 1
        result = "".join(m)
    return result

if __name__ == "__main__":
    orig = "abcdef"
    print "1: " + reverse_v1(orig)      # ver.1
    print "2: " + reverse_v2(orig)      # ver.2
    print "3: " + reverse_v3(orig)      # ver.3
    print "4: " + reverse_v4(orig)      # ver.4
    print "5: " + reverse_v5(orig)      # ver.5
    print "6: " + reverse_v6(orig)      # ver.6
