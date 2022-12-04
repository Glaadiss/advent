# A, X rock, B, Y paper, C, Z scis

bonus_scores = {
    'A': 1,
    'B': 2,
    'C': 3,
}

win_against = {
    'A': 'B',
    'B': 'C',
    'C': 'A'          
}

draw_against = {
    'A': 'A',
    'B': 'B',
    'C': 'C'          
}

lose_against = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

variant = {
    'X': lose_against,
    'Y': draw_against,
    'Z': win_against
}

points = {
    'X': 0,
    'Y': 3,
    'Z': 6
}


with open("./day2/input.txt") as input:
    acc = 0
    plays = [ line.replace('\n', '').split(" ") for line in input.readlines() ]    
    
    for a, b in plays:
        
        v = variant[b]
        p = points[b]
        bonus = bonus_scores[v[a]]   
            
        acc += p + bonus

    print(acc)
    