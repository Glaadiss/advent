import numpy as np
import pprint
from typing import List
from collections import deque 

arr = []
G = {}
starts = []
starts_res = []
with open("./day12/input.txt") as input:
    lines = [line.replace("\n", "") for line in input.readlines()]

    for i, line in enumerate(lines):
        arr.append([])
        for j, letter in enumerate(line):
            if letter == "S":
                print("start at", i, j)
                letter = "a"
            if letter == "E":
                print("end at", i, j)
                letter = "z"            
            arr[i].append(letter)
            
            if letter == "a":
                starts.append((i,j))
    # pprint.pprint(arr)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            G[(i, j)] = []
            curr = arr[i][j]

            if i > 0:
                if ord(curr) - ord(arr[i - 1][j]) >= -1:
                    G[(i, j)].append((i - 1, j))
            if i < (len(arr) - 1):
                if ord(curr) - ord(arr[i + 1][j]) >= -1:
                    G[(i, j)].append((i + 1, j))
            if j > 0:
                if ord(curr) - ord(arr[i][j - 1]) >= -1:
                    G[(i, j)].append((i, j - 1))
            if j < (len(arr[i]) - 1):
                if ord(curr) - ord(arr[i][j + 1]) >= -1:
                    G[(i, j)].append((i, j + 1))

    # pprint.pprint(G)


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


for s in starts:    
    # shortest = shortest_path(G, s, (2,5))
    shortest = shortest_path(G, s, (20,91))
    print(len(shortest))
    if len(shortest) > 0:    
        starts_res.append(len(shortest) - 1)

starts_res.sort()
print(starts_res)

"""

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
"""