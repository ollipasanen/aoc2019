def solution():
    with open("input", "r") as f:
        inp = f.readlines()
        inp1 = [x.strip() for x in inp[0].split(",")]
        inp2 = [x.strip() for x in inp[1].split(",")]

    # Day 1

    mv = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    beento = {}

    x, y = 0, 0
    closest = 1e9

    for i in inp1:
        d, f = i[0], int(i[1::])
        for j in range(f):
            x += mv[d][0]
            y += mv[d][1]
            beento[(x, y)] = True

    x, y = 0, 0

    for i in inp2:
        d, f = i[0], int(i[1::])
        for j in range(f):
            x += mv[d][0]
            y += mv[d][1]
            if (x, y) in beento:
                closest = min(closest, abs(x) + abs(y))
    
    print(closest)

    # Day 2

    beento = {}

    x, y = 0, 0
    closest = 1e9

    ts = 1
    for k, i in enumerate(inp1):
        d, f = i[0], int(i[1::])
        for j in range(f):
            x += mv[d][0]
            y += mv[d][1]
            beento[(x, y)] = ts
            ts += 1

    x, y = 0, 0
    ts = 1

    for k, i in enumerate(inp2):
        d, f = i[0], int(i[1::])
        for j in range(f):
            x += mv[d][0]
            y += mv[d][1]
            if (x, y) in beento:
                closest = min(closest, beento[(x, y)] + ts)
            ts += 1

    print(closest)


if __name__ == '__main__':
    solution()