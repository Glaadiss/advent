import numpy as np
import pprint
from typing import List
from collections import deque 


arr = []
G = {}
starts = []
starts_res = []

def comp(a, b):
    if type(a) == int and type(b) == int:
        if a > b:
            return False
        if b > a:            
            return True
        
        return None
    
    if type(a) == list and type(b) != list:
        b = [b]
    if type(a) != list and type(b) == list:
        a = [a]        
        
        
    for l, r in list(zip(a,b)):
        r = comp(l ,r)
        if r != None:
            return r
            

    if len(a) > len(b):
        return False
    
    return True
    
    

with open("./day13/input.txt") as input:
    lines = [line.replace("\n", "") for line in input.readlines()]
    acc = 0

    for i, (a,b) in enumerate(list(zip(lines[0::3], lines[1::3])), start=1):
        # print(i, eval(a), eval(b))
        if comp(eval(a),eval(b)):
            acc += i
            print(i)
            
    print(acc)
            
    # for i, line in enumerate(lines):
    