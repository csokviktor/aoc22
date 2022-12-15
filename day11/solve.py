import re

lines = [line.strip() for line in open("./day11/inputs.txt", "r").readlines()]


def buildmonkeys():
    monkeys = {}
    for i in range(0, len(lines), 7):
        id = int(re.findall("\d+", lines[i])[0])
        items = [int(i) for i in re.findall("\d+", lines[i + 1])]
        operation = lines[i + 2]
        div = int(re.findall("\d+", lines[i + 3])[0])
        iftrue = int(re.findall("\d+", lines[i + 4])[0])
        iffalse = int(re.findall("\d+", lines[i + 5])[0])
        monkeys[id] = {
            "items": items,
            "operation": operation,
            "div": div,
            "true": iftrue,
            "false": iffalse,
            "inspected": 0,
        }
    return monkeys


def solve1(m):
    for i in range(20):
        for key, value in m.items():
            for item in value.get("items"):
                operation = value.get("operation")
                try:
                    operationCount = int(re.findall("\d+", operation)[0])
                    if "*" in operation:
                        operationcntr = item * operationCount
                    else:
                        operationcntr = item + operationCount
                except:
                    if "*" in operation:
                        operationcntr = item * item
                    else:
                        operationcntr = item + item
                wl = operationcntr // 3
                if (wl % value.get("div")) == 0:
                    m[value.get("true")]["items"].append(wl)
                else:
                    m[value.get("false")]["items"].append(wl)
                m[key]["inspected"] += 1
            m[key]["items"] = []
    inspected = []
    for key in m.keys():
        inspected.append(m[key].get("inspected"))

    inspected.sort(reverse=True)
    print(inspected[0] * inspected[1])


def solve2(m):
    cm = 1
    for k in m.keys():
        cm *= m[k].get("div")

    for i in range(10000):
        for key, value in m.items():
            for item in value.get("items"):
                operation = value.get("operation")
                try:
                    operationCount = int(re.findall("\d+", operation)[0])
                    if "*" in operation:
                        operationcntr = item * operationCount
                    else:
                        operationcntr = item + operationCount
                except:
                    if "*" in operation:
                        operationcntr = item * item
                    else:
                        operationcntr = item + item
                wl = operationcntr
                wl %= cm
                if (wl % value.get("div")) == 0:
                    m[value.get("true")]["items"].append(wl)
                else:
                    m[value.get("false")]["items"].append(wl)
                m[key]["inspected"] += 1
            m[key]["items"] = []
    inspected = []
    for key in m.keys():
        inspected.append(m[key].get("inspected"))

    inspected.sort(reverse=True)
    print(inspected[0] * inspected[1])


monks = buildmonkeys()
solve1(monks)
solve2(monks)
