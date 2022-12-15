line = [line for line in open("./inputs.txt", "r").readlines()][0]


def solve(checkindex):
    for i in range(checkindex, len(line)):
        sublist = line[i-checkindex:i]
        if len(set(sublist)) == len(sublist):
            print(i)
            break

solve(4)
solve(14)