import numpy as np
import pprint

def main():
    X = [1]
    with open("./day10/input.txt") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
        for line in lines:
            currX = X[-1] if len(X) > 0 else 1
            if line.startswith("noop"):                
                X.append(currX) 
            elif line.startswith("addx"):            
                _, numb = line.split(" ")
                numb = int(numb)
                X.append(currX)
                X.append(X[-1] + numb)
                
            if 210 < len(X) < 222:
                print(len(X), line, X[-1])

    # strength_sum = 0
    sprite_pos = []
    draw_pos = []
    result = []
    i = 0
    for x in X:
        
        #sprite pos is x
        #draw pos is i        
        if x == i or (x-1) == i or (x+1) == i:
            result.append("#")
        else:
            result.append(".")
        
        i +=1
        if len(result) == 40:
            print("".join(result[:40]))            
            result = []
            i = 0


if __name__ == "__main__":
    main()