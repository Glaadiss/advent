def get_code(l):
    if ord(l) >= ord('a') and ord(l) <= ord('z'):
        return ord(l) - ord('a') + 1
        
    if ord(l) >= ord('A') and ord(l) <= ord('Z'):
        return ord(l) - ord('A') + 27
    
    return 0


with open("./day3/input.txt") as input:
    acc = 0
    lines = [line.replace('\n', '') for line in input.readlines()]
    for line in lines:
        first, second = line.split()
        
        ion = list(set(first) & set(second))
        for i in ion:
            acc += get_code(ion[0])

    print(acc)
    