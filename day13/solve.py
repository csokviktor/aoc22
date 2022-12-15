from functools import cmp_to_key
from itertools import zip_longest

lines = [line.strip() for line in open("./inputs.txt", "r").readlines()]


pairs = []
packets = []


def parse():
    tempPair = []
    for line in lines:
        if line == "":
            pairs.append(tempPair)
            tempPair = []
            continue
        packets.append(eval(line))
        tempPair.append(eval(line))


def solveInteger(intL, intR):
    if intL < intR:
        return 1
    elif intL > intR:
        return -1


def solveList(listL, listR):
    for elementL, elementR in zip_longest(listL, listR):
        if elementL is None:
            return 1
        elif elementR is None:
            return -1

        if isinstance(elementL, int) and isinstance(elementR, int):
            res = solveInteger(elementL, elementR)
        elif isinstance(elementL, list) and isinstance(elementR, int):
            res = solveList(elementL, [elementR])
        elif isinstance(elementL, int) and isinstance(elementR, list):
            res = solveList([elementL], elementR)
        elif isinstance(elementL, list) and isinstance(elementR, list):
            res = solveList(elementL, elementR)

        if res is not None:
            return res


def solve1():
    global pairs
    cntr = 0
    res = 0
    for l, r in pairs:
        cntr += 1
        if solveList(l, r) == 1:
            res += cntr
    print(res)


def solve2(p: list):
    p.append([[2]])
    p.append([[6]])
    p = sorted(p, key=cmp_to_key(lambda p1, p2: solveList(p1, p2)), reverse=True)
    r = 1
    for i, packet in enumerate(p):
        if packet == [[2]] or packet == [[6]]:
            r *= i + 1

    print(r)


parse()
solve1()
solve2(packets)
