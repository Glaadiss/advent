import numpy as np
import pprint

m = []

with open("./day8/input.txt") as input:
    lines = [line.replace("\n", "") for line in input.readlines()]
    for line in lines:
        m.append([])
        for cell in line:
            m[len(m) - 1].append(int(cell))
            
m = np.array(m)
     
     
def check_if_higher(i, j):
    c = m[i,j] 
    all_left = m[i][0:j]
    all_right = m[i][j+1:m.shape[1]]
    all_top = m[0:i, j]
    all_down = m[i+1:m.shape[0], j]
    return all(c > all_left) or all(c >all_right) or  all(c >all_top) or  all(c >all_down)
    
# matrix = np.loadtxt('./day8/input.txt', delimiter="") 
# print(matrix.shape)
edges = 2 * m.shape[0] + 2 * m.shape[1] - 4

trees_inside = 0

for i in range(1, m.shape[1]-1):
    for j in range(1, m.shape[0]-1):        
        c = m[i][j]        
        if check_if_higher(i, j):            
            print(f"{i} {j} {c} visible" )
            trees_inside +=1
            
print(trees_inside+edges)
         