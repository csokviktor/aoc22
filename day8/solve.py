import math
data = [list(map(int, list(line.strip()))) for line in open("./inputs.txt", "r").readlines()]



def solve1():
    cntr = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            # check if visible
            if y == 0 or y == (len(data) - 1):
                cntr += 1
                continue
            elif x == 0 or x == (len(data[y]) - 1):
                cntr += 1
                continue
            else:
                # check left
                for xi in range(x, 0, -1):
                    if data[y][xi-1] >= data[y][x]:
                        break
                else:
                    cntr += 1
                    continue

                # check right
                for xi in range(x+1, len(data[y])):
                    if data[y][xi] >= data[y][x]:
                        break
                else:
                    cntr += 1
                    continue
                
                # check top
                for yi in range(y, 0, -1):
                    if data[yi-1][x] >= data[y][x]:
                        break
                else:
                    cntr += 1
                    continue

                # check bottom
                for yi in range(y+1, len(data[y])):
                    if data[yi][x] >= data[y][x]:
                        break
                else:
                    cntr += 1
                    continue
    print(cntr)

def solve2():
    scenic = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            # check if visible
            if y == 0 or y == (len(data) - 1):
                continue
            elif x == 0 or x == (len(data[y]) - 1):
                continue
            else:
                cntr = [0, 0, 0, 0]
                # check left
                for xi in range(x, 0, -1):
                    cntr[0] += 1
                    if data[y][xi-1] >= data[y][x]:
                        break

                # check right
                for xi in range(x+1, len(data[y])):
                    cntr[1] += 1
                    if data[y][xi] >= data[y][x]:
                        break
                
                # check top
                for yi in range(y, 0, -1):
                    cntr[2] += 1
                    if data[yi-1][x] >= data[y][x]:
                        break

                # check bottom
                for yi in range(y+1, len(data[y])):
                    cntr[3] += 1
                    if data[yi][x] >= data[y][x]:
                        break
                
                if math.prod(cntr) > scenic:
                    scenic = math.prod(cntr)
    print(scenic)

solve1()
solve2()