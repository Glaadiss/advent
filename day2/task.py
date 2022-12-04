# A, X rock, B, Y paper, C, Z scis

bonus_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

win_against = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'          
}

draw_against = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'          
}


with open("./day2/input.txt") as input:
    acc = 0
    plays = [ line.replace('\n', '').split(" ") for line in input.readlines() ]    
    
    for a, b in plays:
        acc += bonus_scores[b]
        
        if win_against[a] == b:
           acc += 6
           
        if draw_against[a] == b:
           acc += 3
    
    print(acc)
    