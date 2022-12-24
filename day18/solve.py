from collections import deque

lines = [line.strip() for line in open("./day18/inputs.txt", "r").readlines()]


sides = set()
for line in lines:
    x, y, z = line.split(",")
    sides.add((int(x), int(y), int(z)))


moves = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

minx = min([x for x, y, z in sides]) - 5
maxx = max([x for x, y, z in sides]) + 5
miny = min([y for x, y, z in sides]) - 5
maxy = max([y for x, y, z in sides]) + 5
minz = min([z for x, y, z in sides]) - 5
maxz = max([z for x, y, z in sides]) + 5


def solve1():
    ans = 0
    for (x, y, z) in sides:
        for mx, my, mz in moves:
            dx, dy, dz = x + mx, y + my, z + mz
            if (dx, dy, dz) not in sides:
                ans += 1

    print(ans)


def isbuble(side: set, bubbles: set, notbubbles: set):

    # check previous results to make it faster
    if side in bubbles:
        return True
    elif side in notbubbles:
        return False

    visited = set()
    deqsides = deque([side])
    while deqsides:
        deqside = deqsides.popleft()
        if (deqside in sides) or (deqside in visited):
            continue
        visited.add(deqside)

        # check if we are too far away from the cube as we are checking from inside out
        # if deqside[0] not in range(-150, 150):
        #     notbubbles.update(visited)
        #     return True
        # if deqside[1] not in range(-150, 150):
        #     notbubbles.update(visited)
        #     return True
        # if deqside[2] not in range(-150, 150):
        #     notbubbles.update(visited)
        #     return True
        if len(visited) > 1373:
            # add the visited to not bubbles as we reached out trough them
            notbubbles.update(visited)
            return False
        for mx, my, mz in moves:
            deqsides.append((deqside[0] + mx, deqside[1] + my, deqside[2] + mz))

    # If we could not reach out we are in a bubble
    bubbles.update(visited)
    return True


def solve2():
    ans = 0
    bubbles = set()
    notbubbles = set()
    for (x, y, z) in sides:
        for mx, my, mz in moves:
            if not isbuble((x + mx, y + my, z + mz), bubbles, notbubbles):
                ans += 1

    print(ans)


solve1()
solve2()
