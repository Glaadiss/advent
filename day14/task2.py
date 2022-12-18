import numpy as np
import pprint
from typing import List

    
def print_state(state):
    for x in state:
        print("".join(x))           

    

with open("./day14/input.txt") as input:
    lines = [line.replace("\n", "") for line in input.readlines()]
    acc = 0
    
    all_cords = []

    for line in lines:
        cords = []
        c = line.split(" -> ")
        for x in c:
            cords.append([int(i) for i in x.split(",")])

        pairs = list(zip(cords[0:-1], cords[1:]))
        for p in pairs:
            x1, y1 = p[0]
            x2, y2 = p[1]            
            all_cords.append((x2, y2))
            while x2 != x1:
                if x2 > x1:
                    x2 -= 1            
                else: 
                    x2 += 1            
                all_cords.append((x2, y2))
            while y2 != y1:
                
                if y2 > y1:
                    y2 -= 1
                else:
                    y2 += 1
                all_cords.append((x2, y2))
    unique_cords = np.unique(all_cords, axis=0)
    
    max_x = max(unique_cords[:, 0])
    min_x = min(unique_cords[:, 0])
    max_y = max(unique_cords[:, 1])
    min_y = min(unique_cords[:, 1])
    
    
    state = []
    for y in range(0, max_y + 1):
        state.append([])
        for x in range(min_x, max_x + 1):
            if (x, y) in [tuple(u) for u in unique_cords]:
                state[len(state) - 1].append("#")
            else:
                state[len(state) - 1].append(".")        

    
    
    
    snow = [[500, 0, False]]
    snow_np = np.array(snow)
    abyss = False
    while abyss == False:
        for s in snow:
            s_x, s_y, rest = s
            if rest:
                continue
            s_x_scaled = s_x - min_x

            if len(state) > (s_y+1):
                if state[s_y + 1][s_x_scaled] == ".":
                    state[s_y][s_x_scaled] = "."
                    state[s_y + 1][s_x_scaled] = "+"
                    s[0] = s_x
                    s[1] = s_y + 1                                
                
                elif s_x_scaled > 0 and state[s_y + 1][s_x_scaled - 1] == ".":
                    state[s_y][s_x_scaled] = "."
                    state[s_y + 1][s_x_scaled - 1] = "+"      
                    s[0] = s_x - 1
                    s[1] = s_y + 1                                  

                elif s_x_scaled < (len(state[s_y + 1]) - 1) and state[s_y + 1][s_x_scaled + 1] == ".":
                    state[s_y][s_x_scaled] = "."
                    state[s_y + 1][s_x_scaled +1] = "+"
                    s[0] = s_x + 1
                    s[1] = s_y + 1
                elif s_y == 0:
                # elif (s_x_scaled-1) < 0  or (s_x_scaled + 1) == len(state[s_y]):
                    abyss = True                                    
                else:
                    s[2] = True 
                    print(sum(np.array(snow)[:, 2]))   
                    snow.append([500, 0, False]) 
                    
                
            
        # if state[0][500 - min_x] == ".":
            
            # state[0][500 - min_x] = "+":                     

    print_state(state)
    print(sum(np.array(snow)[:, 2]) + 1)    

                    
            
            # try: 
            #     if state[s_y + 1][s_x_scaled - 1]:
            #         ...
            # except:
            #     ...
            # try: 
            #     if state[s_y + 1][s_x_scaled]:
            #         ...
            # except:
            #     ...
            # try: 
            #     if state[s_y + 1][s_x_scaled]:
            #         ...
            # except:
            #     ...                
            
            
        
    
    