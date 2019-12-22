class OrbitNode:
    def __init__(self, c):
        self.name = c
        self.parent = None
        self.children = []

    def __repr__(self):
        return "OrbitNode<{}>".format(self.name)

def solution():
    with open("input", "r") as f:
        inp = [x.strip() for x in f.readlines()]

    node = {}

    for r in inp:
        a, _, b = r.partition(")")

        if a not in node:
            node[a] = OrbitNode(a)

        if b not in node:
            node[b] = OrbitNode(b)

        node[b].parent = node[a]
        node[a].children.append(node[b])

    # Day 1

    def rec(node, depth):
        if not node.children:
            return depth

        cnt = depth

        for v in node.children:
            cnt += rec(v, depth + 1)

        return cnt

    print(rec(node["COM"], 0))

    # Day 2

    def rec(node, l, d):
        if not node.parent:
            return l

        return rec(node.parent, l + [(node, d)], d+1)

    t1 = {k: v for k, v in rec(node["YOU"], [], 0)}

    for n, _ in rec(node["SAN"], [], 0):
        if n in t1:
            print(t1[n] + _ - 2)
            break

if __name__ == '__main__':
    solution()