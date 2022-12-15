import re
from typing import List
lines = [line for line in open("./inputs.txt", "r").readlines()]

def parseStack(l):
    retList = []
    for i in range(0,len(l)+1,4):
        if i == 0:
            continue
        retList.append(l[i-3])
    return retList


def getData():
    stacks = [[] for _ in range(len(parseStack(lines[0])))]
    moves = []
    stackparsed = False
    for line in lines:
        if line.strip() == "":
            stackparsed = True
            for i in range(len(stacks)):
                stacks[i].pop()
            continue
        if not stackparsed:
            for i, s in enumerate(parseStack(line)):
                if s != " ":
                    stacks[i].append(s)
        else:
            match = re.findall(r'\d+', line.strip())
            moves.append([int(m) for m in match])
    
    return moves, stacks

def solve1(mvs, stk: List[list]):
    for cntr, fr, to in mvs:
        for _ in range(cntr):
            element = stk[fr-1].pop(0)
            stk[to-1].insert(0, element)
    
    print(''.join([element[0] for element in stk]))


def solve2(mvs, stk: List[list]):
    for cntr, fr, to in mvs:
        elements = [stk[fr-1].pop(0) for _ in range(cntr)]
        elements = [elements[i] for i in range(len(elements)-1, -1, -1)]
        for element in elements:
            stk[to-1].insert(0, element)
    
    print(''.join([element[0] for element in stk]))


m, t = getData()
solve2(m, t)