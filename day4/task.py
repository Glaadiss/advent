with open("./day4/input.txt") as input:
    acc = 0
    lines = [line.replace("\n", "") for line in input.readlines()]
    for line in lines:
        a, b = line.split(",")

        a1, a2 = a.split("-")
        b1, b2 = b.split("-")

        a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)

        set_a = list(range(a1, a2 + 1))
        set_b = list(range(b1, b2 + 1))

        ion = list(set(set_a) & set(set_b))

        if len(ion) > 0:
            acc += 1

    print(acc)
