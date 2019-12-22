from itertools import permutations

class HaltException(Exception): pass
class InputException(Exception): pass

class Runner:
    def __init__(self, program, inputs=None, print_ret=True):
        self.program = program
        self.inputs = inputs
        self.input_i = 0
        self.print = print_ret
        self.outputs = []
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
            try:
                self.step()
            except HaltException as e:
                return True

    def run_until_no_input(self):
        while True:
            try:
                self.step()
            except InputException as e:
                return False
            except HaltException:
                return True

    def step(self):
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
            if self.inputs is None:
                self.program[a] = int(input())
            else:
                if self.input_i >= len(self.inputs):
                    self.i -= 2
                    raise InputException

                self.program[a] = self.inputs[self.input_i]
                self.input_i += 1
        elif opcode == 4:
            a = self.read(C)

            if self.print:
                print(a)

            self.outputs.append(a)
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
            raise HaltException
        else:
            print("Unhandled opcode")
            raise HaltException

    def last_output(self):
        if not self.outputs:
            return None

        return self.outputs[-1]


def solution():
    with open("input", "r") as f:
        inp = [int(x) for x in f.read().strip().split(",")]

    # Day 1

    mout = 0
    for perm in permutations(list(range(0, 5))):
        out = 0
        for phase in perm:
            p = [x for x in inp]
            r = Runner(p, inputs=[phase, out], print_ret=False)
            r.run()
            out = r.outputs[0]
        mout = max(mout, out)

    print(mout)

    # Day 2

    mout = 0
    for seq in permutations(list(range(5, 10))):
        runners = [Runner([x for x in inp], inputs=[seq[x]], print_ret=False) for x in range(5)]

        out = 0

        while True:
            stop = False

            for i, r in enumerate(runners):
                r.inputs.append(out)
                halted = r.run_until_no_input()
                out = r.last_output()
                if halted:
                    stop = True

            if stop:
                break

        mout = max(mout, out)

    print(mout)

if __name__ == '__main__':
    solution()