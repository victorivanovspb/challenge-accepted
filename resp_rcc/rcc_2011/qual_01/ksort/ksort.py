# -*- coding: utf-8 -*-
import sys
import random

def parse_integers(msg):
    result = list()
    mass = msg.split(" ")
    for i in mass:
        result.append(int(i))
    return result

def coin_toss():
    return True if random.randint(1, 2) == 1 else False

def mix(mass, k):
    for idx, el in enumerate(mass):
        mix_el = coin_toss()
        if mix_el and idx + k < len(mass):
            el2 = mass[idx + k]
            mass[idx + k] = el
            mass[idx] = el2

def get_el_group_by_k(mass, start_pos, k):
    result = []
    pos = start_pos
    while pos < len(mass): # go right to end
        result.append(mass[pos])
        pos += k
    pos = start_pos - k
    while pos >= 0:
        result.append(mass[pos])
        pos -= k
    return result

def check_mass(mass, k, sorted_mass):
    for idx, el in enumerate(mass):
        fault = True
        
        m = get_el_group_by_k(mass, idx, k)
        #print m
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
        
def count_kgroup(mass, k, g): # g - group shift
    "Целевая функция"
    if len(mass) == 1:
        return 0
    min_pos = find_min_pos(mass)
    del mass[min_pos]
    return min_pos + count_kgroup(mass, k, g)
    
if __name__ == "__main__":
    
    #mass = [3, 0, 12, 77, 20, 5, 41, 8, 16, 13, 2, 2, 2, 99, 1, 81, 105, 4, 33, 36, 17, 105, 33]
    #sorted_mass = list(mass)
    #sorted_mass.sort(key=int)
    #mixed_mass = list(sorted_mass)
    #k = 3
    #mix(mixed_mass, k)
    #print mass
    #print sorted_mass
    #print mixed_mass

    #mixed_mass = mass = [6, 10, 4, 1, 2]
    #mixed_mass = [40, 70, 17, 36, 34, 6, 61, 27, 69, 16, 46, 41, 12, 57, 28, 28, 4, 45, 75, 56, 7, 72, 72, 53, 38, 50, 42, 33, 21, 61, 63, 64, 21, 15, 51, 25, 8, 77]
    n = int(sys.stdin.readline().strip('\n'))
    msg = sys.stdin.readline().strip('\n') 
    mixed_mass = parse_integers(msg)
    k = int(sys.stdin.readline().strip('\n'))
  
    sorted_mass = list(mixed_mass)
    sorted_mass.sort(key=int)

    if check_mass(mixed_mass, k, sorted_mass):
        #print "check_mass() get True"
        
        sum_val = 0
        for g in xrange(k):
            gmass = get_el_group_by_k(mixed_mass, g, k)
            sum_val += count_kgroup(gmass, k, g)
        sys.stdout.write(str(sum_val))
        #print str(sum_val)
            
    else:
        sys.stdout.write(str(-1))
        #print str(-1)
    