commands = [line.strip() for line in open("./inputs.txt", "r").readlines()]

"""
{
    name: a
    size: none
    subElements: [
        {
            name: b
            size: aa
            subelements
        }
    ]
}
"""
def buildFolderStruct():
    currentDirectory = []
    directory = {}
    for c in commands:
        if c.startswith("$ cd"):
            c = c.replace("$ cd ", "")
            if c == "..":
                currentDirectory.pop()
            else:
                dict = directory
                for dir in currentDirectory:
                    dict = dict[dir]
                dict[c] = {"files": [], "size": 0}
                currentDirectory.append(c) 
        if c.startswith("ls"):
            continue
        if c[0].isdigit():
            size, name = c.split(" ")
            dict = directory
            for dir in currentDirectory:
                dict = dict[dir]
            dict["files"].append((int(size), name))
    return directory

defaultkeys = ["files", "size"]

def buildSize(built: dict) -> int:
    if sorted(built.keys()) != defaultkeys:
        currentSize = 0
        for key in built.keys():
            if key not in defaultkeys:
                currentSize += buildSize(built[key])
        built["size"] = currentSize + sum([element[0] for element in built["files"]])
        return built["size"]
    else:
        built["size"] += sum([element[0] for element in built["files"]])
        return sum([element[0] for element in built["files"]])

def returnSize(built: dict, sl: list):
    sl.append(built["size"])
    if sorted(built.keys()) != defaultkeys:
        for key in built.keys():
            if key not in defaultkeys:
                returnSize(built[key], sl)

def solve1(b: dict):
    sizelist = []   
    returnSize(b, sizelist)
    cntr1 = 0
    for r in sizelist:
        if r <= 100000:
            cntr1 += r
    print(cntr1)

def solve2(b: dict):
    sizelist = []
    free = 70000000 - b["size"]
    requiredfree = 30000000 - free
    returnSize(b, sizelist)
    sortedres = sorted(sizelist)
    for r in sortedres:
        if r > requiredfree:
            print(r)
            break
    

builtDirectory = buildFolderStruct()
buildSize(builtDirectory["/"])
solve1(builtDirectory["/"])
solve2(builtDirectory["/"])