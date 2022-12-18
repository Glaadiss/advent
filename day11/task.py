import numpy as np
import pprint
from typing import List
old = 0
class Monkey:
    def __init__(self, id, items: List[int], m1_ind, m2_ind, div_by, operator, new_quant):
        self.id = id
        self.items = items
        self.m1_ind = m1_ind
        self.m2_ind = m2_ind
        self.div_by = div_by
        self.operator = operator
        self.new_quant = new_quant
        self.inspect_time = 0
    
    def op(self, state):
        self.inspect_time += 1
        quant = state if self.new_quant == "old" else int(self.new_quant)
        if self.operator == "+":
            return state + quant
        
        return state * quant
        
        
    # def action_when_div(self, state, monkeys):                            
    #     if len(monkeys[self.id].items) > 0:
    #         # item = monkeys[self.id].items.pop()
    #         if state % self.div_by == 0:
    #             monkeys[self.m1_ind].items.append(item)
    #         else:
    #             monkeys[self.m2_ind].items.append(item)

monkeys: List[Monkey] = []   

with open("./day11/input.txt") as input:
    lines = [line.replace("\n", "") for line in input.readlines()]
    for i, line in enumerate(lines):
          
        if i % 7 == 0:
            items = lines[i+1].split("Starting items:")[-1]
            items = items.split(", ")
            items = [int(i) for i in items]
            op = lines[i+2].split("old ")[-1].split(" ")                      
            div_by = lines[i+3].split("by ")[-1]
            div_by = int(div_by)
            m1_ind = lines[i+4].split("monkey ")[-1]
            m1_ind = int(m1_ind)
            m2_ind = lines[i+5].split("monkey ")[-1]
            m2_ind = int(m2_ind)                    
            m = Monkey(int(i/7), items, m1_ind, m2_ind, div_by, op[0], op[1])
            
            monkeys.append(m)
            

          
# pprint.pprint(monkeys)

    
for i in range(70):
    for m in monkeys:
        while len(m.items) > 0:
            item = m.items.pop(0)
            level = m.op(item)
            level = int(level/3)
            # m.action_when_div(level, monkeys)
            if level % m.div_by == 0:
                monkeys[m.m1_ind].items.append(level)
            else:
                monkeys[m.m2_ind].items.append(level)        
      

inspect_times = [m.inspect_time for m in monkeys]
inspect_times.sort(reverse=True)
print(inspect_times)
print(inspect_times[0] * inspect_times[1])
        
for m in monkeys:
    print(m.__dict__)