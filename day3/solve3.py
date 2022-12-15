sacks = [line.strip() for line in open("./inputs.txt", "r").readlines()]

def solve1():
    cntr = 0
    for sack in sacks:
        middle=len(sack)//2
        first_half=sack[:middle]
        sec_half=sack[middle:]
        match: str = [sec for sec in sec_half if sec in first_half][0]
        cntr += ord(match) - 96 if match.islower() else ord(match) - 64 + 26
    
    print(cntr)

def solve2():
    groups  = [sacks[i:i+3] for i in range(0, len(sacks), 3)]
    cntr = 0
    for group in groups:
        match =  [i for i in group[0] if i in group[1] and i in group[2]][0]
        print(match)
        print(ord(match) - 96 if match.islower() else ord(match) - 64 + 26)
        cntr += ord(match) - 96 if match.islower() else ord(match) - 64 + 26

    print(cntr)
solve1()
solve2()