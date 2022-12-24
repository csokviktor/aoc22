from collections import deque, defaultdict

lines = [line.strip() for line in open("./day24/inputs.txt", "r").readlines()]

rows = len(lines) - 2
columns = len(lines[0]) - 2

moves = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}


def moveblizards(blizards):
    for b in blizards:
        x, y, (dx, dy) = b
        x = x + dx
        y = y + dy

        # do wall check
        x = x % columns
        if x == 0:
            x = columns
        if x > columns:
            x = 1
        y = y % rows
        if y == 0:
            y = rows
        if y > rows:
            y = 1

        b[0] = x
        b[1] = y
    return blizards


def solve(blizards, part2=False):
    start = (1, 0)
    end = (120, 26)
    # end = (6, 5)
    q = deque()
    # states (start), round1done, round2done, dist
    q.append((start, False, False, 0))
    distances = defaultdict()
    distances[start] = 0
    maxdist = -1
    visited = set()
    tocheck = set()
    while True:
        (x, y), r1done, r2done, dist = q.popleft()
        if (x, y) == end and not part2:
            print(dist)
            break
        if (x, y) == end and r1done and r2done:
            print(dist)
            break
        # could move
        if dist > maxdist:
            maxdist = dist
            blizards = moveblizards(blizards)
            tocheck = set([(x, y) for x, y, _ in blizards])

        for dx, dy in list(moves.values()) + [(0, 0)]:
            nx, ny = x + dx, y + dy
            if (
                (nx, ny) not in tocheck
                and nx in range(1, columns + 1)
                and ny in range(1, rows + 1)
                or (nx, ny) == start
                or (nx, ny) == end
            ):
                if (nx, ny, r1done, r2done, dist) not in visited:
                    visited.add((nx, ny, r1done, r2done, dist))
                    if (nx, ny) == end:
                        q.append(((nx, ny), True, r2done, dist + 1))
                    elif (nx, ny) == start and r1done:
                        q.append(((nx, ny), r1done, True, dist + 1))
                    else:
                        q.append(((nx, ny), r1done, r2done, dist + 1))


blizards = [
    [x, y, moves.get(lines[y][x])]
    for y in range(1, len(lines) - 1)
    for x in range(1, len(lines[0]) - 1)
    if lines[y][x] != "."
]
solve(blizards)
blizards = [
    [x, y, moves.get(lines[y][x])]
    for y in range(1, len(lines) - 1)
    for x in range(1, len(lines[0]) - 1)
    if lines[y][x] != "."
]
solve(blizards, True)
