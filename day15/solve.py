import re

lines = [line.strip() for line in open("./inputs.txt", "r").readlines()]


def manhattan(a, b):
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))


beacons = []
sensors = []
for line in lines:
    lt = re.findall("-?\d+\.?\d*", line)
    lt = [int(l) for l in lt]
    d = abs(lt[0] - lt[2]) + abs(lt[1] - lt[3])
    sensors.append((lt[0], lt[1], d))
    beacons.append((lt[2], lt[3]))


def valid(x, y, sensors):
    for (sx, sy, d) in sensors:
        dxy = abs(x - sx) + abs(y - sy)
        if dxy <= d:
            return False
    return True


def solve1():
    cntr = 0
    for x in range(-10000000, 10000000):
        y = 2000000
        if not valid(x, y, sensors) and (x, y) not in beacons:
            cntr += 1
    print(cntr)


def get_edges(sensor):
    ret = set()
    sx, sy, d = sensor
    for dx in range(d + 2):
        dy = (d + 1) - dx
        for px, py in [(-1, 1), (1, -1), (1, 1), (-1, -1)]:
            x = sx + (dx * px)
            y = sy + (dy * py)
            ret.add((x, y))

    return ret


def solve2():
    for sensor in sensors:
        edges = get_edges(sensor)
        for x, y in edges:
            if not (0 <= x <= 4000000 and 0 <= y <= 4000000):
                continue
            if valid(x, y, sensors):
                return x * 4000000 + y


solve1()
print(solve2())
