# -*- coding: utf-8 -*-
import sys

def parse_integers(msg):
    result = list()
    mass = msg.split(" ")
    for i in mass:
        result.append(int(i))
    return result

def get_el_group_by_k(mass, start_pos, k):
    result = []
    pos = start_pos
    while pos < len(mass):      # идём от старта до конца списка...
        result.append(mass[pos])
        pos += k
    pos = start_pos - k
    while pos >= 0:             # ...идём от старта до начала списка
        result.append(mass[pos])
        pos -= k
    return result

def check_mass(mass, k, sorted_mass):
    for idx, el in enumerate(mass):
        fault = True
        m = get_el_group_by_k(mass, idx, k)
        for elj in m:
            if sorted_mass[idx] == elj:
                fault = False
        if fault:
            return False
    return True

def find_min_pos(mass):
    min_val = 0
    min_pos = -1
    for idx, value in enumerate(mass):
        if min_pos == -1:
            min_pos = idx
            min_val = value
        elif value < min_val:
            min_pos = idx
            min_val = value
    return min_pos  
        
def count_kgroup(mass, k): # Целевая функция
    "Выполняется подсчёт k-перестановок, необходимых для сортировки списка."
    if len(mass) == 1:
        return 0
    min_pos = find_min_pos(mass)
    del mass[min_pos]
    return min_pos + count_kgroup(mass, k)
    
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip('\n'))
    mixed_mass = parse_integers(sys.stdin.readline().strip('\n'))
    k = int(sys.stdin.readline().strip('\n'))
  
    sorted_mass = list(mixed_mass)
    sorted_mass.sort(key=int)

    if check_mass(mixed_mass, k, sorted_mass):
        sum_val = 0
        for g in xrange(k):
            gmass = get_el_group_by_k(mixed_mass, g, k)
            sum_val += count_kgroup(gmass, k)
        sys.stdout.write(str(sum_val))
    else:
        sys.stdout.write(str(-1))
