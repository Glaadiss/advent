import numpy as np
import pprint

def dir_from_pos(dir, p):
    if len(p) == 0:
        if "__files__" not in dir:
            dir["__files__"] = {}
        return dir
        
    if p[0] not in dir:
        dir[p[0]] = {}
    
    dir = dir[p[0]]
    return dir_from_pos(dir, p[1:])
        
    


tree = { "/" : {} }
with open("./day7/input.txt") as input:
    lines = [line.replace("\n", "") for line in input.readlines()]
    current_pos = ["/"]
    search_mode = False
    current_dir = {}
    for line in lines:
        if line.startswith("$ cd"):
            search_mode = False
            _, _, pos = line.split(" ")
            if pos == "/":
                current_pos = ["/"]
            elif pos == "..":
                current_pos = current_pos[:-1] 
            else:
                current_pos.append(pos)
                
            current_dir = dir_from_pos(tree, current_pos)
                
            
        elif line.startswith("$ ls"):
            search_mode = True
        elif line.startswith("dir"):
            _, dir_name = line.split(" ")
        else:
            size, filename = line.split(" ")
            size = int(size)
            current_dir["__files__"][filename] = size
            
less_t = []
def find_size(KEY, t):
    
    s = 0
    for t_key in t:
        if t_key == "__files__":
            for key in t["__files__"]:
                s += t["__files__"][key]            
        else:
            s += find_size(t_key, t[t_key])
    
    print(KEY, s)
    if s < 100000:
        less_t.append(s)
    return s


find_size("/", tree) 
print(sum(less_t))

# pprint.pprint(tree)


    
    



# a = input[:-3]
# b = input[1:-2]
# c = input[2:-1]
# d = input[3:]


# for i, items in enumerate(zip(a, b, c, d)):
#     print(i, items)
#     if len(np.unique(items)) == 4:
#         print(i + 4)        
#         break
