import math

commands = [line.strip() for line in open("./day9/inputs.txt", "r").readlines()]

moves = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}


def solve1():
    hcord = [0, 0]
    tcord = [0, 0]
    tpositions = []
    for move in commands:
        m, count = move.split(" ")
        count = int(count)
        for _ in range(count):
            if tcord not in tpositions:
                tpositions.append([k for k in tcord])
            hcord = [sum(x) for x in zip(hcord, moves.get(m))]

            xdiff = hcord[0] - tcord[0]
            ydiff = hcord[1] - tcord[1]
            if abs(xdiff) <= 1 and abs(ydiff) <= 1:
                pass
            elif abs(xdiff) >= 2 and abs(ydiff) >= 2:
                tcord[0] = hcord[0] - 1 if tcord[0] < hcord[0] else hcord[0] + 1
                tcord[1] = hcord[1] - 1 if tcord[1] < hcord[1] else hcord[1] + 1
            elif abs(xdiff) >= 2:
                tcord[0] = hcord[0] - 1 if tcord[0] < hcord[0] else hcord[0] + 1
                tcord[1] = hcord[1]
            elif abs(ydiff) >= 2:
                tcord[0] = hcord[0]
                tcord[1] = hcord[1] - 1 if tcord[1] < hcord[1] else hcord[1] + 1
            if tcord not in tpositions:
                tpositions.append([k for k in tcord])

    print(len(tpositions))


def solve2():
    coords = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
    ]
    tpositions = []
    for move in commands:
        m, count = move.split(" ")
        count = int(count)
        for _ in range(count):
            if coords[-1] not in tpositions:
                tpositions.append([k for k in coords[-1]])
            coords[0] = [sum(x) for x in zip(coords[0], moves.get(m))]

            for i in range(1, 10):
                xdiff = coords[i - 1][0] - coords[i][0]
                ydiff = coords[i - 1][1] - coords[i][1]
                if abs(xdiff) <= 1 and abs(ydiff) <= 1:
                    pass
                elif abs(xdiff) >= 2 and abs(ydiff) >= 2:
                    coords[i][0] = (
                        coords[i - 1][0] - 1
                        if coords[i][0] < coords[i - 1][0]
                        else coords[i - 1][0] + 1
                    )
                    coords[i][1] = (
                        coords[i - 1][1] - 1
                        if coords[i][1] < coords[i - 1][1]
                        else coords[i - 1][1] + 1
                    )
                elif abs(xdiff) >= 2:
                    coords[i][0] = (
                        coords[i - 1][0] - 1
                        if coords[i][0] < coords[i - 1][0]
                        else coords[i - 1][0] + 1
                    )
                    coords[i][1] = coords[i - 1][1]
                elif abs(ydiff) >= 2:
                    coords[i][0] = coords[i - 1][0]
                    coords[i][1] = (
                        coords[i - 1][1] - 1
                        if coords[i][1] < coords[i - 1][1]
                        else coords[i - 1][1] + 1
                    )
                if coords[-1] not in tpositions:
                    tpositions.append([k for k in coords[-1]])

    print(len(tpositions))


solve1()
solve2()
