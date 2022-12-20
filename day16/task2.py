import numpy as np
import re
import copy


# VISITED = {}
CACHE = {}
# CACHE
calc = 0
hit_cache = 0
# 246
next_move = "" 
MAX_T = 26
  
def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return [] 
    
def find_paths(d: dict):
    simple_d = { i: d[i]["valves"] for i in d}
    good_valves = [i for i in d if d[i]["pressure"] !=0 or i == "AA"]
    pressures = { i: d[i]["pressure"] for i in d }
    new_d = {}
    for i in good_valves:        
        new_d[i] = {}
        for j in good_valves:
            if i == j:
                continue
            new_d[i][j] = -1
            
    
    for i in good_valves:
        for j in good_valves:
            if i != j:
                new_d[i][j] = len(shortest_path(simple_d, i,j))

    
    return new_d, pressures



def open_valve(paths, pressures, curr1, curr2, t1, t2, opened):
    if (t1 <= 0 and t2 <= 0) or len(pressures) == len(opened):
        return 0
    
    opts = []
    for p in paths[curr1]:
        for k in paths[curr2]:
            if p == k:
                continue
            if p in opened or k in opened:
                continue        
            time_needed_1 = paths[curr1][p]
            time_needed_2 = paths[curr2][k]
            
            remain_time_1 = t1 - time_needed_1
            remain_time_2 = t2 - time_needed_2
            
            all_presure = 0
            if remain_time_1 >= 0 and remain_time_2 >= 0:
                valve_pressure_1 = remain_time_1 * pressures[p]    
                valve_pressure_2 = remain_time_2 * pressures[k]
                all_presure = valve_pressure_1 + valve_pressure_2 + open_valve(paths, pressures, p, k, remain_time_1, remain_time_2, opened + [p, k])        
                
            # elif remain_time_1 >= 0:
            #     valve_pressure_1 = remain_time_1 * pressures[p]    
            #     all_presure = valve_pressure_1 + open_valve(paths, pressures, p, k, remain_time_1, t2, opened + [p])                        
            # elif remain_time_2 >= 0:
            #     valve_pressure_2 = remain_time_2 * pressures[p]    
            #     all_presure = valve_pressure_2 + open_valve(paths, pressures, p, k, t1, remain_time_2, opened + [k])                                        
                
            
            
            opts.append(all_presure)

    if len(opts) == 0:
        return 0
    
    return max(opts)
    
     

def main():
    with open("./day16/input.txt") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
        rates = [int(re.findall("-?\d+\.?\d*", line)[0]) for line in lines]
        valves = [line.split(" ")[1] for line in lines]
        next_valves = [
            line.split("valve")[1].replace("s", "").lstrip().split(", ")
            for line in lines
        ]
        data = list(zip(rates, valves, next_valves))
        # opened = []
        # for d in data:
        #     if d[0] == 0:
        #         opened.append(d[1])
                
        data_dict = {
            d[1]: {"pressure": d[0], "valves": d[2], "closed": True} for d in data
        }
        
        paths, pressures = find_paths(data_dict)
        
        best_pressure = open_valve(paths, pressures, "AA", "AA", 26, 26, ["AA"] )
        print(best_pressure)

if __name__ == "__main__":
    main()
