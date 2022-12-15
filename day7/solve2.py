commands = [line.strip() for line in open("./inputs.txt", "r").readlines()]

def buildFolderStruct():
    currentDirectory = []
    directory = {}
    for c in commands:
        if c.startswith("$ cd"):
            c = c.replace("$ cd ", "")
            if c == "..":
                currentDirectory.pop()
            else:
                currentDirectory.append(c)
                directory["".join(currentDirectory)] = []
        if c.startswith("ls"):
            continue
        if c[0].isdigit():
            size, _ = c.split(" ")
            directory["".join(currentDirectory)].append(int(size))
    return directory

directory = buildFolderStruct()

def solve1(d):
    weights = []
    for key, items in d.items():
        cntr = 0
        for k, i in d.items():
            if key in k:
                cntr += sum(i)
        
        weights.append(cntr)
    
    cntr1 = 0
    for r in weights:
        if r <= 100000:
            cntr1 += r
    print(cntr1)


def solve2(d):
    weights = []
    for key, items in d.items():
        cntr = 0
        for k, i in d.items():
            if key in k:
                cntr += + sum(i)
        
        weights.append(cntr)
    
    sortedres = sorted(weights)
    free = 70000000 - sortedres[-1]
    requiredfree = 30000000 - free
    for r in sortedres:
        if r > requiredfree:
            print(r)
            break
solve1(directory)
solve2(directory)