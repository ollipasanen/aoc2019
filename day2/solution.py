class Runner:
    def __init__(self, program):
        self.program = program
        self.i = 0

    def read(self):
        op = self.program[self.i]
        self.i += 1
        return op

    def peek(self):
        return self.program[self.i]

    def run(self):
        while True:
            opcode = self.read()

            if opcode == 1:
                a, b, c = self.read(), self.read(), self.read()
                self.program[c] = self.program[a] + self.program[b]
            elif opcode == 2:
                a, b, c = self.read(), self.read(), self.read()
                self.program[c] = self.program[a] * self.program[b]
            elif opcode == 99:
                return


def solution():
    with open("input", "r") as f:
        inp = [int(x) for x in f.read().strip().split(",")]

    # Day 1
    p = [x for x in inp]
    p[1] = 12
    p[2] = 2
    r = Runner(p)
    r.run()
    print(r.program[0])

    # Day 2
    for noun in range(100):
        for verb in range(100):
            p = [x for x in inp]

            p[1] = noun
            p[2] = verb

            # Day 1
            r = Runner(p)
            r.run()

            if r.program[0] == 19690720:
                print(noun * 100 + verb)
                return

if __name__ == '__main__':
    solution()