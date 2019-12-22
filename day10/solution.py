import copy
import time
import math

from functools import cmp_to_key

def solution():
    with open("input", "r") as f:
        inp = [x.strip() for x in f.readlines()]

    # Day 1 

    asteroid_pos = []
    free_pos = []

    for cy in range(len(inp)):
        for cx in range(len(inp[0])):
            c = inp[cy][cx]

            if c == "#":
                asteroid_pos.append((cx, cy))
            elif c == ".":
                free_pos.append((cx, cy))

    # Day 1

    def gcd(a, b): 
        if b == 0:
            return a 
        return gcd(b, a%b)

    width = len(inp[0])
    height = len(inp)

    def visible_from(cx, cy):
        removed = {}
        cnt = 0

        for x, y in asteroid_pos:
            if (x, y) in removed:
                continue

            if x == cx and cy == y:
                continue

            cnt += 1

            dx = x - cx
            dy = y - cy

            g = gcd(abs(dx), abs(dy))

            dx //= g
            dy //= g

            tx = cx
            ty = cy

            while True:
                tx += dx
                ty += dy

                if tx >= width or ty >= height or tx < 0 or ty < 0:
                    break

                l = inp[ty][tx]
                if l == "#":
                    removed[(tx, ty)] = True

        return cnt

    mtaken = 0
    lx, ly = -1, -1

    for cx, cy in asteroid_pos:
        v = visible_from(cx, cy)

        if v > mtaken:
            mtaken = v
            lx = cx
            ly = cy

    print(mtaken)

    # Day 2

    asteroid_pos.remove((lx, ly))
    target = 200
    remove_cnt = 0

    while True:
        closest_visible = []
        diff = {}

        for x, y in asteroid_pos:
            kx = x - lx
            ky = y - ly
            g = gcd(abs(kx), abs(ky))
            dx = kx // g
            dy = ky // g

            if (dx, dy) not in diff:
                diff[(dx, dy)] = (kx, ky)
            else:
                ex, ey = diff[(dx, dy)]
                if ex*ex+ey*ey > kx*kx+ky*ky:
                    diff[(dx, dy)] = (kx, ky)

        def ang(p):
            y = p[0] - lx
            x = (p[1] - ly)
            return (math.atan2(y, x))

        current_pass = sorted(((lx+dx, ly+dy) for (dx, dy) in diff.values()), key=ang, reverse=True)

        for cx, cy in current_pass:
            asteroid_pos.remove((cx, cy))
            remove_cnt += 1
            if remove_cnt == target:
                print(cx*100+cy)
                return


if __name__ == '__main__':
    solution()