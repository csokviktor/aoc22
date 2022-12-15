lines = [line.strip() for line in open("./day14/inputs.txt", "r").readlines()]


def buildRocks():
    rocks = set()
    for line in lines:
        prev = None
        for point in line.split("->"):
            x, y = point.split(",")
            x, y = int(x), int(y)
            if (x, y) not in rocks:
                rocks.add((x, y))
            if prev is not None:
                dx = x - prev[0]
                dy = y - prev[1]
                diff = max(abs(dx), abs(dy))
                for i in range(diff):
                    nx = prev[0] + i * (1 if dx > 0 else (-1 if dx < 0 else 0))
                    ny = prev[1] + i * (1 if dy > 0 else (-1 if dy < 0 else 0))
                    rocks.add((nx, ny))
            prev = (x, y)

    return rocks


def solve(rocks: set):
    floor = 2 + max(r[1] for r in rocks)
    for x in range(-100000, 100000):
        rocks.add((x, floor))

    p1solved = False
    for i in range(1000000):
        rock = (500, 0)
        while True:
            if rock[1] + 1 >= floor and (not p1solved):
                p1solved = True
                print(i)
            if (newrock := (rock[0], rock[1] + 1)) not in rocks:
                rock = newrock
            elif (newrock := (rock[0] - 1, rock[1] + 1)) not in rocks:
                rock = newrock
            elif (newrock := (rock[0] + 1, rock[1] + 1)) not in rocks:
                rock = newrock
            else:
                break
        if rock == (500, 0):
            print(i + 1)
            break
        rocks.add(rock)


rocks = buildRocks()
solve(rocks)
