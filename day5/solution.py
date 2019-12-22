class Runner:
    def __init__(self, program):
        self.program = program
        self.i = 0

    def read(self, mode="1"):
        op = self.program[self.i]

        if mode == "0":
            op = self.program[op]

        self.i += 1
        return op

    def peek(self):
        return self.program[self.i]

    def run(self):
        while True:
            fmt = "{:05}".format(self.read())
            opcode = int(fmt[3:5])
            C, B, A = fmt[2], fmt[1], fmt[0]

            if opcode == 1:
                a, b, c = self.read(C), self.read(B), self.read()
                self.program[c] = a + b
            elif opcode == 2:
                a, b, c = self.read(C), self.read(B), self.read()
                self.program[c] = a * b
            elif opcode == 3:
                a = self.read()
                self.program[a] = int(input())
            elif opcode == 4:
                a = self.read(C)
                print(a)
            elif opcode == 5:
                a, b = self.read(C), self.read(B)
                if a:
                    self.i = b
            elif opcode == 6:
                a, b = self.read(C), self.read(B)
                if not a:
                    self.i = b
            elif opcode == 7:
                a, b, c = self.read(C), self.read(B), self.read()
                self.program[c] = int(a < b)
            elif opcode == 8:
                a, b, c = self.read(C), self.read(B), self.read()
                self.program[c] = int(a == b)
            elif opcode == 99:
                return
            else:
                print("Unhandled opcode")
                return



def solution():
    with open("input", "r") as f:
        inp = [int(x) for x in f.read().strip().split(",")]

    # Day 1
    p = [x for x in inp]
    r = Runner(p)
    r.run()

if __name__ == '__main__':
    solution()