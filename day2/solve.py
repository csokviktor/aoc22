
RES_MAPPING = {
    ("A", "X"): 1,
    ("A", "Y"): 2,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 1,
    ("B", "Z"): 2,
    ("C", "X"): 2,
    ("C", "Y"): 0,
    ("C", "Z"): 1
}
VAL_MAPPING = {"X": 1, "Y": 2, "Z": 3}

rounds = [line.strip() for line in open("./inputs.txt", "r").readlines()]

def solve1():
    cntr = 0
    
    for round in rounds:
        op, me = round.split(" ")
        res = RES_MAPPING.get((op, me))
        cntr += VAL_MAPPING.get(me)
        cntr += res*3
    
    print(cntr)

def solve2():
    cntr = 0

    for round in rounds:
        op, expected = round.split(" ")
        if expected == "X": expected = 0
        elif expected == "Y": expected = 1
        elif expected == "Z": expected = 2
        for key, val in RES_MAPPING.items():
            if op == key[0] and val == expected:
                cntr += expected*3
                cntr += VAL_MAPPING.get(key[1])
    print(cntr)

solve1()
solve2()