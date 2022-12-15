data = [line.strip() for line in open("./inputs.txt", "r").readlines()]


def solve1():
    x = 1
    xprev = [1]
    for line in data:
        if "noop" in line:
            xprev.append(x)
        elif "addx" in line:
            _, xplus = line.split(" ")
            xplus = int(xplus)
            for i in range(1):
                xprev.append(x)
            x += xplus
            xprev.append(x)

    print(xprev)
    res = 0
    for j in [20, 60, 100, 140, 180, 220]:
        res += xprev[j - 1] * j

    print(res)
    return xprev


def shiftcart(middle: int):
    return [middle - 1, middle, middle + 1]


def solve2(prev):
    rcntr = 0
    ccntr = 0
    cartpos = [0, 1, 2]
    immage = [[], [], [], [], [], [], []]
    for data in prev:
        cartpos = shiftcart(data)
        if ccntr in cartpos:
            immage[rcntr].append("#")
        else:
            immage[rcntr].append(".")
        ccntr += 1
        if ccntr == 40:
            ccntr = 0
            rcntr += 1
    for line in immage:
        print("".join(line))


prevxpos = solve1()
solve2(prevxpos)
