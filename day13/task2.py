import numpy as np
import pprint
from typing import List
from collections import deque 
from functools import cmp_to_key

arr = []
G = {}
starts = []
starts_res = []

def comp(a, b):
    if type(a) == int and type(b) == int:
        if a > b:
            return -1
        if b > a:            
            return 1
        
        return 0
    
    if type(a) == list and type(b) != list:
        b = [b]
    if type(a) != list and type(b) == list:
        a = [a]        
        
        
    for l, r in list(zip(a,b)):
        res = comp(l ,r)
        if res != 0:
            return res            

    if len(a) > len(b):
        return -1
    
    if len(b) > len(a):
        return 1
        
    if len(a) == len(b):
        return 0
    
    
    # print("a, b:", a,b, list(zip(a,b)))
    

res = comp( [[1], [2, 3, 4]],                       [1, [2, [3, [4, [5, 6, 0]]]], 8, 9] )
res2 =comp( [1, [2, [3, [4, [5, 6, 0]]]], 8, 9] ,  [[1], [2, 3, 4]])

with open("./day13/input.txt") as input:
    lines = [line.replace("\n", "") for line in input.readlines()]
    lines = [eval(line) for line in lines if line != ""]

    lines.append([[2]])

    lines.append([[6]])
    
    
    
    new_lines = sorted(lines, key=cmp_to_key(comp), reverse=True)
    
    for i, x in enumerate(new_lines):        
        print(i, x)

    print(new_lines.index([[6]]), new_lines[new_lines.index([[6]])])
    print(new_lines.index([[2]]), new_lines[new_lines.index([[2]])])
    
    print( (new_lines.index([[6]]) + 1) * (new_lines.index([[2]]) + 1) )
    # print((new_lines.index([[2]]) + 1) * (new_lines.index([[6]]) + 1))
    # for i, (a,b) in enumerate(list(zip(lines[0::3], lines[1::3])), start=1):
    #     # print(i, eval(a), eval(b))
    #     if comp(eval(a),eval(b)):
    #         acc += i
    #         print(i)
            
    # print(acc)
            
    # for i, line in enumerate(lines):
    
    """
    []
    [[]]
    [[[]]]
    [1,1,3,1,1]
    [1,1,5,1,1]
    [[1],[2,3,4]]
    [1,[2,[3,[4,[5,6,0]]]],8,9]
    [1,[2,[3,[4,[5,6,7]]]],8,9]
    [[1],4]
    [[2]]
    [3]
    [[4,4],4,4]
    [[4,4],4,4,4]
    [[6]]
    [7,7,7]
    [7,7,7,7]
    [[8,7,6]]
    [9]
    """