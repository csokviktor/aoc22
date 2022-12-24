from typing import Dict
import sys

lines = [line.strip() for line in open("./day21/inputs.txt", "r").readlines()]


def build():
    cmds = {}
    for line in lines:
        name = line[0 : line.index(":")]
        cmd = line.split(":")[1].strip()
        cmds[name] = cmd

    return cmds


def solve(cmds: Dict[str, str], name: str, humnval: int) -> int:
    if name == "humn" and humnval >= 0:
        return humnval

    cmd = cmds.get(name)
    if cmd.isdigit():
        return int(cmd)
    else:
        # dfs shit here
        left, op, right = cmd.split()
        leftval = solve(cmds, left, humnval)
        rightval = solve(cmds, right, humnval)
        if op == "+":
            return leftval + rightval
        elif op == "-":
            return leftval - rightval
        elif op == "/":
            return leftval // rightval
        elif op == "*":
            return leftval * rightval


def solve2(cmds):
    rootleft, _, rootright = cmds["root"].split()
    mod = (solve(cmds, rootleft, 1) - solve(cmds, rootright, 1)) > 0
    lowbound = 0
    highbound = sys.maxsize

    while lowbound < highbound:
        mid = (lowbound + highbound) // 2
        diff = solve(cmds, rootleft, mid) - solve(cmds, rootright, mid)
        if not diff:
            print(mid)
            break
        if diff > 0:
            if mod:
                lowbound = mid
            else:
                highbound = mid
        else:
            if mod:
                highbound = mid
            else:
                lowbound = mid


def demo(cmds):
    p1, _, p2 = cmds["root"].split()
    if solve(cmds, p2, 0) != solve(cmds, p2, 1):
        p1, p2 = p2, p1

    target = solve(cmds, p2, 0)

    lo = 0
    hi = int(1e20)
    while lo < hi:
        mid = (lo + hi) // 2
        score = target - solve(cmds, p1, mid)
        if score < 0:
            lo = mid
        elif score == 0:
            print(mid)
            break
        else:
            hi = mid


cmds = build()

# part1
print(solve(cmds, "root", -1))

# part2
solve2(cmds)
demo(cmds)
