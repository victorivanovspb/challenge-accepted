# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    line = sys.stdin.readline()
    
    result = list("")
    sub = list("")
    sub_mode = False
    for ch in line:
        if sub_mode:
            if ch == ")":
                result.extend(sub)
                del sub[:]
                sub_mode = False
            else:
                sub.insert(0, ch)
        else:
            if ch == "(":
                sub_mode = True
            else:
                result.append(ch)
    
    sys.stdout.write("".join(result))        
