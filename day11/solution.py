from itertools import permutations

class HaltException(Exception): pass
class InputException(Exception): pass

MODE_POSITION = "0"
MODE_IMMEDIATE = "1"
MODE_RELATIVE = "2"

class Runner:
    def __init__(self, program, inputs=None, print_ret=True):
        self.program = {i: v for i, v in enumerate(program)}
        self.inputs = inputs
        self.input_i = 0
        self.print = print_ret
        self.outputs = []
        self.i = 0
        self.relbase = 0

    def read(self, mode=MODE_IMMEDIATE):
        if self.i not in self.program:
            self.program[self.i] = 0

        op = self.program[self.i]

        if mode == "0":
            if op not in self.program:
                self.program[op] = 0

            op = self.program[op]

        if mode == "2":
            op += self.relbase

            if op not in self.program:
                self.program[op] = 0

            op = self.program[op]

        self.i += 1
        return op

    def write(self, addr, val, mode="0"):

        if mode == "1":
            raise Exception("Bad mode for write")
        elif mode == "2":
            addr += self.relbase

        self.program[addr] = val

    # def peek(self):
    #     return self.program[self.i]

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
        fmt = "{:05}".format(self.read("1"))
        opcode = int(fmt[3:5])
        C, B, A = fmt[2], fmt[1], fmt[0]

        if opcode == 1:
            a, b, c = self.read(C), self.read(B), self.read()
            self.write(c, a + b, A)
        elif opcode == 2:
            a, b, c = self.read(C), self.read(B), self.read()
            self.write(c, a * b, A)
        elif opcode == 3:
            a = self.read()
            if self.inputs is None:
                self.write(a, int(input()), C)
            else:
                if self.input_i >= len(self.inputs):
                    self.i -= 2
                    raise InputException

                self.write(a, self.inputs[self.input_i], C)
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
            self.write(c, int(a < b), A)
        elif opcode == 8:
            a, b, c = self.read(C), self.read(B), self.read()
            self.write(c, int(a == b), A)
        elif opcode == 9:
            self.relbase += self.read(C)
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

    # Part 1

    dir = (0, 1)
    pos = (0, 0)
    panels = {}

    r = Runner([x for x in inp], inputs=[], print_ret=False)

    while True:
        if pos not in panels:
            cur_col = 0
        else:
            cur_col = panels[pos]

        # run
        r.inputs.append(cur_col)
        halted = r.run_until_no_input()

        if halted:
            break

        new_color, rotate = r.outputs[-2:]

        # paint tile
        panels[pos] = new_color

        # rotate and step
        if rotate == 0:
            dir = (-dir[1], dir[0])
        else:
            dir = (dir[1], -dir[0])

        pos = (pos[0] + dir[0], pos[1] + dir[1])

    print(len(panels))

    # Part 2

    panels = {}
    r = Runner([x for x in inp], inputs=[1], print_ret=False)

    while True:
        halted = r.run_until_no_input()

        if halted:
            break

        new_color, rotate = r.outputs[-2:]

        # paint tile
        panels[pos] = new_color

        # rotate and step
        if rotate == 0:
            dir = (-dir[1], dir[0])
        else:
            dir = (dir[1], -dir[0])

        pos = (pos[0] + dir[0], pos[1] + dir[1])

        if pos not in panels:
            cur_col = 0
        else:
            cur_col = panels[pos]

        # run
        r.inputs.append(cur_col)

    x_low, x_hi = min(x[0] for x in panels), max(x[0] for x in panels)
    y_low, y_hi = min(x[1] for x in panels), max(x[1] for x in panels)

    for y in range(y_low, y_hi+1):
        for x in range(x_hi, x_low, -1):
            pos = (x, y)

            if pos in panels and panels[pos] == 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()


if __name__ == '__main__':
    solution()