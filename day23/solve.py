from collections import defaultdict
from typing import Set

lines = [line.strip() for line in open("./day23/inputs.txt", "r").readlines()]


def build():
    elves = set()
    for y, line in enumerate(lines):
        for x, el in enumerate(line):
            if el == "#":
                elves.add((x, y))
    return elves


def solve(elves: Set[int]):

    dirs = ["N", "S", "W", "E"]
    for i in range(10000000000):

        # store elves that want to move to same pos
        nextmoves = defaultdict(list)

        for x, y in elves:
            # check if has neighbour
            hasNeighbour = False
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if ((dx != 0) or (dy != 0)) and (x + dx, y + dy) in elves:
                        hasNeighbour = True
            if not hasNeighbour:
                continue

            # do the check porcess
            moved = False  # check for all possible moves until one is not found
            for dir in dirs:
                if moved:
                    continue
                if (
                    dir == "N"
                    and (x + 1, y - 1) not in elves
                    and (x, y - 1) not in elves
                    and (x - 1, y - 1) not in elves
                ):
                    nextmoves[(x, y - 1)].append((x, y))
                    moved = True
                elif (
                    dir == "W"
                    and (x - 1, y - 1) not in elves
                    and (x - 1, y) not in elves
                    and (x - 1, y + 1) not in elves
                ):
                    nextmoves[(x - 1, y)].append((x, y))
                    moved = True
                elif (
                    dir == "S"
                    and (x - 1, y + 1) not in elves
                    and (x, y + 1) not in elves
                    and (x + 1, y + 1) not in elves
                ):
                    nextmoves[(x, y + 1)].append((x, y))
                    moved = True
                elif (
                    dir == "E"
                    and (x + 1, y - 1) not in elves
                    and (x + 1, y) not in elves
                    and (x + 1, y + 1) not in elves
                ):
                    nextmoves[(x + 1, y)].append((x, y))
                    moved = True

        # rotate moves
        dirs = dirs[1:] + [dirs[0]]

        canmove = False
        for nextpos, elvestomove in nextmoves.items():
            if len(elvestomove) == 1:
                elves.discard(elvestomove[0])
                elves.add(nextpos)
                canmove = True

        if not canmove:
            print(i + 1)
            break

        if i == 9:
            maxX = max(x for x, _ in elves)
            minX = min(x for x, _ in elves)
            maxY = max(y for _, y in elves)
            minY = min(y for _, y in elves)
            ans = 0
            for y in range(minY, maxY + 1):
                for x in range(minX, maxX + 1):
                    if (x, y) not in elves:
                        ans += 1
            print(ans)


elves = build()
solve(elves)
