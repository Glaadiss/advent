import numpy as np
import pprint

# class Cord:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __add__(self, c):
#         return Cord(self.x + c.x, self.y + c.y)
    


# m = []
def main():
    knots = [np.array([0,0]) for i in range(10)]

    t_positions = []


    def follow(i):
        xt, yt = knots[i+1]
        xh, yh = knots[i]
        d_x, d_y = xh - xt, yh - yt

        if d_x > 1:
            xt += 1            
            if d_y > 0:
                yt += 1
            if d_y < 0:
                yt -= 1            
        elif d_x < -1:
            xt -= 1            
            if d_y > 0:
                yt += 1
            if d_y < 0:
                yt -= 1                           
        elif d_y > 1:
            yt += 1
            if d_x > 0:
                xt += 1
            if d_x < 0:
                xt -= 1                 
        elif d_y < -1:
            yt -= 1
            if d_x > 0:
                xt += 1
            if d_x < 0:
                xt -= 1               
            
        knots[i+1][0] = xt
        knots[i+1][1] = yt        
        
        if (i == 8):
            t_positions.append((xt, yt))


    dir_h = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0),
    }

    with open("./day9/input.txt") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
        for line in lines:
            direction, numb = line.split(" ")
            numb = int(numb)

            for i in range(numb):
                knots[0][0] += dir_h[direction][0]
                knots[0][1] += dir_h[direction][1]
                
                for i in range(9):
                    follow(i)

        print(t_positions)
        print(np.unique(t_positions, axis=0))
        print(len(np.unique(t_positions, axis=0)))

if __name__ == "__main__":
    main()