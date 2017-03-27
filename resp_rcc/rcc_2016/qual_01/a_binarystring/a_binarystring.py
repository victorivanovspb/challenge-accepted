# -*- coding: utf-8 -*
import sys

def parse_integers(msg):
    result = list()
    mass = msg.split(" ")
    for i in mass:
        result.append(int(i))
    return result

def fast_check(a, b, c, d): # a=00, b=01, c=10, d=11
    """Быстрые проверки на невозможность построения строки по указанным ключам (a, b, c, d)."""
    # Проверка 1: если имеются подстроки "00" и "11", то должна быть хотя бы одная подстрока "01" или "10".
    if a > 0 and d > 0: 
        if b == 0 and c == 0:
            return False
    # Проверка 1: количества подстрок "01" и "10" не могут различаться больше, чем на 1.
    if abs(b) - abs(c) > 1:
        return False
    return True

def create_0101(b_01, c_10):
    result = ""
    if b_01 == 0 and c_10 == 0:
        return result
    if b_01 >= c_10:
        result += "01" * b_01
        if b_01 == c_10:
            result += "0"
    else:
        result += "10" *c_10
    return result

def get_first(msg, ch):
    for idx, el in enumerate(msg):
        if el == ch:
            return idx
    return -1 

def increase_x_to_xx(source, count, x):
    """В строке (source) первый попавшийся символ (x) заменяется на подстроку из символов (x), имеющую длину (count)."""
    result = ""
    if len(source) == 0:
        if count >= 1:
            result = (x * count) + x
        else:
            result = source
    else:
        pos = get_first(source, x)
        if pos == -1:
            result = source
        else:
            result = source[0:pos] + (x * count) + x + source[pos + 1:]
    return result

def increase_0_to_00(source, count):
    """Например, для source='01010' при count=2 будет '0001010'."""
    return increase_x_to_xx(source, count, "0")

def increase_1_to_11(source, count):
    """Например, для source='01010' при count=2 будет '0111010'."""
    return increase_x_to_xx(source, count, "1")

def count_string(msg):
    """Подсчёт входящих в строку (msg) подстрок '00', '01', '10', '11'."""
    a = 0
    b = 0
    c = 0
    d = 0
    prev = msg[0:1]
    for curr in msg[1:]:
        if prev == "0":
            if curr == "0":
                a += 1
            elif curr == "1":
                b += 1
        elif prev == "1":
            if curr == "0":
                c += 1
            elif curr == "1":
                d += 1
        prev = curr
    return (a, b, c, d)
            
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    
    for i in xrange(n):
        mass = parse_integers(sys.stdin.readline())
        a = mass[0] # 00
        b = mass[1] # 01
        c = mass[2] # 10
        d = mass[3] # 11
        
        if not fast_check(a, b, c, d):
            sys.stdout.write("impossible" + "\n")
            continue
        
        res = create_0101(b, c)
        res = increase_0_to_00(res, a)
        res = increase_1_to_11(res, d)
        sys.stdout.write(res + "\n")
        
        #print "Count=" + str(count_string(res))        
