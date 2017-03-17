# -*- coding: utf-8 -*-
import sys
import math

def parse_integers(msg):
    result = list()
    mass = msg.split(" ")
    for i in mass:
        result.append(int(i))
    return result


if __name__ == "__main__":
    n, m = tuple(parse_integers(sys.stdin.readline()))
    
    rules = list()
    for i in xrange(n):
        rule = sys.stdin.readline()
        c, t, p = tuple(parse_integers(rule))
        rules.append([c, t, p])
    
    calls = parse_integers(sys.stdin.readline())
    min_sum_kop = 0
    min_rule_num = 0
    for idx, rule in enumerate(rules):
        curr_sum_kop = 0 
        for call in calls:
            if rule[1] > call:  # rule minimal time > call time
                continue        # curr_sum += 0
            else:
                k = int(math.floor(call / rule[1]))
                if k * rule[1] < call:
                    k += 1
                curr_sum_kop += k * rule[2] # minimal time price (kop.)
        curr_sum_kop += rule[0] * 100       # abonent (rouble = 100 kop.)
        
        if min_rule_num == 0:
            min_rule_num = idx + 1
            min_sum_kop = curr_sum_kop
        elif curr_sum_kop < min_sum_kop:
            min_rule_num = idx + 1
            min_sum_kop = curr_sum_kop
    
    sys.stdout.write(str(min_rule_num))
