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

def count_trees(c, v):
    j = 0
    for i in v:
        j +=1
        if i >= c:
            return j
    
    return j
            
     
def calc_score(i, j):
    c = m[i,j] 
    all_left = np.flip(m[i][0:j])
    all_right = m[i][j+1:m.shape[1]]
    all_top = np.flip(m[0:i, j])
    all_down = m[i+1:m.shape[0], j]
    return count_trees(c , all_left) * count_trees(c ,all_right) *  count_trees(c ,all_top) *  count_trees(c ,all_down)
    
# matrix = np.loadtxt('./day8/input.txt', delimiter="") 
# print(matrix.shape)
edges = 2 * m.shape[0] + 2 * m.shape[1] - 4

trees_inside = 0

scores = []
for i in range(1, m.shape[1]-1):
    for j in range(1, m.shape[0]-1):        
        c = m[i][j]        
        scores.append(calc_score(i, j))
            
print(max(scores))
         