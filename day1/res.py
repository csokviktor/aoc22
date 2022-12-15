def readFile():
    with open("./inputs.txt", "r") as f:
        return f.readlines()

def solve():
    data = readFile()
    data = [line.strip() for line in data]
    elves = []
    cntr = 0
    for line in data:
        if line != '':
            cntr += int(line)
        else:
            elves.append(cntr)
            cntr = 0
    
    elves.sort(reverse=True)
    print(elves[0])
    print(elves[0]+elves[1]+elves[2])
    


solve()