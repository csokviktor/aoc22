import re
pairs = [line.strip() for line in open("./inputs.txt", "r").readlines()]

def solve():
    cntr1 = 0
    cntr2 = 0
    for pair in pairs:
        match = re.findall(r'\d+', pair.strip())
        match = [int(m) for m in match]
        elfone: set = set(list(range(match[0],match[1]+1)))
        elftwo: set = set(list(range(match[2],match[3]+1)))
        if elfone.issubset(elftwo) or elftwo.issubset(elfone):
            cntr1 += 1
        
        if elfone & elftwo:
            cntr2 += 1
    
    print(cntr1)
    print(cntr2)

solve()