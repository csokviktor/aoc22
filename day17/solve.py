lines = [line.strip() for line in open("./day17/inputs.txt", "r").readlines()]


moves = [*lines[0]]


def getmax(rocks):
    maxY = 0
    for r in rocks:
        for p in r:
            maxY = max(maxY, p[1])
    return maxY


def generatestar(maxY):
    return [(3, maxY + 2), (2, maxY + 1), (3, maxY + 1), (4, maxY + 1), (3, maxY)]


def generateL(maxY):
    return [(2, maxY), (3, maxY), (4, maxY), (4, maxY + 1), (4, maxY + 2)]


def generateI(maxY):
    return [(2, maxY), (2, maxY + 1), (2, maxY + 2), (2, maxY + 3)]


def generateFlat(maxY):
    return [(2, maxY), (3, maxY), (4, maxY), (5, maxY)]


def generateC(maxY):
    return [(2, maxY + 1), (2, maxY), (3, maxY + 1), (3, maxY)]


def getrock(maxy, rgen):
    if rgen % 5 == 0:
        return generateFlat(maxy)
    elif rgen % 5 == 1:
        return generatestar(maxy)
    elif rgen % 5 == 2:
        return generateL(maxy)
    elif rgen % 5 == 3:
        return generateI(maxy)
    elif rgen % 5 == 4:
        return generateC(maxy)


def pushleft(rock):
    if any([x == 0 for (x, _) in rock]):
        return rock
    return [(x - 1, y) for x, y in rock]


def pushright(rock):
    if any([x == 6 for (x, _) in rock]):
        return rock
    return [(x + 1, y) for x, y in rock]


def movedown(rock):
    return [(x, y - 1) for x, y in rock]


def moveup(rock):
    return [(x, y + 1) for x, y in rock]


def checkintersect(rock, rocks):
    for r in rocks:
        for rx, ry in r:
            for rockx, rocky in rock:
                if (rockx == rx) and (rocky == ry):
                    return True
    return False


def checkcollision(rocks, rock):
    for (x, y) in rock:
        if (x, y) in rocks:
            return True
    return False


def solve1(moves):
    rgen = 0
    maxy = 0
    i = 0
    rocks = set([(x, 0) for x in range(7)])
    while rgen < 1000000000000:
        rock = getrock(maxy + 4, rgen)
        while True:
            # simulate movement
            if moves[i] == ">":
                rock = pushright(rock)
                # check if there is collision with others
                if checkcollision(rocks, rock):
                    rock = pushleft(rock)
            elif moves[i] == "<":
                rock = pushleft(rock)
                # check if there is collision with others
                if checkcollision(rocks, rock):
                    rock = pushright(rock)

            # to handle the shorter example
            i = (i + 1) % len(moves)

            rock = movedown(rock)
            if checkcollision(rocks, rock):
                rock = moveup(rock)
                rocks.update(rock)
                maxy = max([y for (_, y) in rocks])
                break

        rgen += 1
        if rgen == 2022:
            print(maxy)

    print(maxy)


solve1(moves)
