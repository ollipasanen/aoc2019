def solution():
    with open("input", "r") as f:
        lines = [int(x.strip()) for x in f.readlines()]

    # Part 1
    total = sum((x//3 - 2) for x in lines)
    print(total)

    # Part 2
    def fuel(mass, total):
        r = mass//3 - 2
        if r < 0:
            return total
        return fuel(r, total + r)

    total = sum(fuel(x, 0) for x in lines)
    print(total)

if __name__ == '__main__':
    solution()