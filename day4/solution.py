def solution():
    with open("input", "r") as f:
        a, b = [int(x) for x in f.read().split("-")]


    # Day 1

    cnt = 0

    for i in range(a, b+1):
        double = False
        prev = -1
        bad = False

        while i:
            k = i % 10

            if k == prev:
                double = True

            if prev != -1 and prev < k:
                bad = True
                break

            i //= 10
            prev = k

        if bad or not double:
            continue

        cnt += 1

    print(cnt)

    # Day 2

    cnt = 0

    for i in range(a, b+1):
        double = True
        bad = False

        l = []

        while i:
            l = [(i%10)] + l
            i //= 10

        p = []
        cur = ""

        for j in range(6):
            if cur and l[j-1] != l[j]:
                p.append(cur)
                cur = ""

            if j > 0:
                if l[j] < l[j-1]:
                    bad = True

            cur += str(l[j])

        p.append(cur)

        if not bad and any(len(x) == 2 for x in p):
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    solution()