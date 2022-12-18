from queue import LifoQueue

stackStr = """
        [H]         [S]         [D]
    [S] [C]         [C]     [Q] [L]
    [C] [R] [Z]     [R]     [H] [Z]
    [G] [N] [H] [S] [B]     [R] [F]
[D] [T] [Q] [F] [Q] [Z]     [Z] [N]
[Z] [W] [F] [N] [F] [W] [J] [V] [G]
[T] [R] [B] [C] [L] [P] [F] [L] [H]
[H] [Q] [P] [L] [G] [V] [Z] [D] [B]"""

lists = [
    'HTZD',
    'QRWTGCS',
    'PBFQNRCH',
    'LCNFHZ',
    'GLFQS',
    'VPWZBRCS',
    'ZFJ',
    'DLVZRHQ',
    'BHGNFZLD'
]

stacks = []
for i in range(len(lists)):
    stacks.append(LifoQueue())
    for item in lists[i]:
        stacks[i].put(item)


cmds = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def run_cmd(cmd):
    """
    e.g
    move 4 from 8 to 7
    """
    words = cmd.split(" ")

    number, f, t = int(words[1]), int(words[3]), int(words[5])
    print(cmd)
    print(number, f, t)
    buffer = LifoQueue()
    for i in range(number):
        # print(stacks[f-1].qsize(), stacks[t-1].qsize())
        if stacks[f - 1].qsize() > 0:            
            buffer.put(stacks[f - 1].get())
            # stacks[t - 1].put(stacks[f - 1].get())
    for i in range(number):
        # print(stacks[f-1].qsize(), stacks[t-1].qsize())
        if buffer.qsize() > 0:            
            stacks[t - 1].put(buffer.get())


with open("./day5/input.txt") as input:
    acc = 0
    lines = [line.replace("\n", "") for line in input.readlines()]
    for cmd in lines:
        print(cmd)
        run_cmd(cmd)

    result = ""
    for s in stacks:
        if s.qsize() > 0:
            result += str(s.get())
        # else: 
        #     result += " "
            
    print(result)
    # print(lines[1].split(" "))
    # for line in lines:
    #     a, b = line.split(",")

    #     a1, a2 = a.split("-")
    #     b1, b2 = b.split("-")

    #     a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)

    #     set_a = list(range(a1, a2 + 1))
    #     set_b = list(range(b1, b2 + 1))

    #     ion = list(set(set_a) & set(set_b))

    #     if len(ion) > 0:
    #         acc += 1

    # print(acc)
