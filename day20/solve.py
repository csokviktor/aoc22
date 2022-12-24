from typing import List

lines = [line.strip() for line in open("./day20/inputs.txt", "r").readlines()]


class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.prev: Node = None
        self.next: Node = None


def build():
    nodes: List[Node] = []
    for line in lines:
        nodes.append(Node(int(line)))

    for i in range(1, len(nodes)):
        nodes[i - 1].next = nodes[i]
        nodes[i].prev = nodes[i - 1]

    nodes[-1].next = nodes[0]
    nodes[0].prev = nodes[-1]

    return nodes


def solve(nodes: List[Node], nodecpy: List[Node]):
    # rotate all nodes
    for i in range(len(nodes)):
        # extract node with pointers
        nodes[i].prev.next = nodes[i].next
        nodes[i].next.prev = nodes[i].prev

        movecntr = nodecpy[i].val % (len(nodes) - 1)
        # movecntr = nodecpy[i].val
        # r = abs(movecntr) takes too much time, must need modulo
        # -2 mod 6 = 4
        p = nodes[i].prev
        n = nodes[i].next
        for _ in range(movecntr):
            # shift pointers
            p = p.next
            n = n.next

        # reset pointers
        p.next = nodes[i]
        n.prev = nodes[i]
        nodes[i].prev = p
        nodes[i].next = n
    return nodes


def calcres(nodes: List[Node]):
    res = 0
    for i in range(len(nodes)):
        if nodes[i].val == 0:
            cur = nodes[i]
            for i in range(3):
                for _ in range(1000):
                    cur = cur.next
                res += cur.val
    return res


def solve1(nodes: List[Node]):

    nodecpy = nodes[:]
    nodes = solve(nodes, nodecpy)
    print(calcres(nodes))


def solve2(nodes: List[Node]):
    for n in nodes:
        n.val = 811589153 * n.val

    for _ in range(10):
        nodecpy = nodes[:]
        nodes = solve(nodes, nodecpy)

    print(calcres(nodes))


nodes = build()
tosolve = 1
if tosolve == 1:
    solve1(nodes)
else:
    solve2(nodes)
