def get_code(l):
    if ord(l) >= ord('a') and ord(l) <= ord('z'):
        return ord(l) - ord('a') + 1
        
    if ord(l) >= ord('A') and ord(l) <= ord('Z'):
        return ord(l) - ord('A') + 27
    
    return 0


with open("./day3/input.txt") as input:
    acc = 0
    lines = [line.replace('\n', '') for line in input.readlines()]
    
    for x in range(int(len(lines) / 3)):
        
        # for line in lines[]
        # first, second = line[:int(len(line)/2)], line[int(len(line)/2):]        
        # ion = list(set(first) & set(second))
                
        first, second, third = lines[x*3], lines[x*3+1], lines[x*3+2]
        ion = list(set(first) & set(second) & set(third))                     
        print(ion)
        acc += get_code(ion[0])


    print(acc)
    