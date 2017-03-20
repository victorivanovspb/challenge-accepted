# -*- coding: utf-8 -*-
import sys

def parse_integers(msg):
    result = list()
    mass = msg.split(" ")
    for i in mass:
        result.append(int(i))
    return result

def list_to_str(mass):
    msg = ""
    for el in mass:
        msg += str(el) + " "
    msg = msg.strip()
    return msg

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    f_mass = parse_integers(sys.stdin.readline())
    
    sumf = 0
    for f in f_mass:
        sumf += f
    
    boss = int(sumf/2)
    boss_id = -1
    for idx, f in enumerate(f_mass):
        if f == boss:
            boss_id = idx
    if boss_id != -1:
        f_mass.pop(boss_id)
        f_mass.insert(len(f_mass), boss)
    
    sys.stdout.write(list_to_str(f_mass))
