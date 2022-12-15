from collections import deque


lines = [line.strip() for line in open("./day12/inputs.txt", "r").readlines()]

R = len(lines)
C = len(lines[0])

transformed = [[0 for _ in range(C)] for _ in range(R)]


def transform():
    global transformed
    for r in range(R):
        for c in range(C):
            if lines[r][c] == "S":
                transformed[r][c] = 1
            elif lines[r][c] == "E":
                transformed[r][c] = 26
            else:
                transformed[r][c] = ord(lines[r][c]) - ord("a") + 1


def bfs(part=1):
    global transformed
    currentNodes = deque()
    for r in range(R):
        for c in range(C):
            if (part == 1 and lines[r][c] == "S") or (
                part == 2 and transformed[r][c] == 1
            ):
                currentNodes.append(((r, c), 0))

    visited = set()
    while currentNodes:
        (r, c), distance = currentNodes.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if lines[r][c] == "E":
            return distance

        for (x, y) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nr = r + x
            nc = c + y
            if (
                0 <= nr < R
                and 0 <= nc < C
                and transformed[nr][nc] - 1 <= transformed[r][c]
            ):
                currentNodes.append(((nr, nc), distance + 1))


transform()
print(bfs())
print(bfs(2))
