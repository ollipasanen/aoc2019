# from typing import Tuple
from dataclasses import dataclass

import copy
import subprocess

from math import gcd
from functools import reduce

@dataclass
class Vec3:
    x: int
    y: int
    z: int

    def __add__(self, b):
        return Vec3(self.x + b.x, self.y + b.y, self.z + b.z)

    def __getitem__(self, i) -> int:
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        elif i == 2:
            return self.z
        raise ValueError("Bad Index {}".format(i))

    def __eq__(self, b):
        return self.x == b.x and self.y == b.y and self.z == b.z

@dataclass
class Moon:
    pos: Vec3
    vel: Vec3

    def gravity(self, another) -> Vec3:
        def diff(a: int, b: int) -> int:
            if a < b:
                return 1
            elif a > b:
                return -1
            else:
                return 0

        return Vec3(diff(self.pos[0], another.pos[0]),
                    diff(self.pos[1], another.pos[1]),
                    diff(self.pos[2], another.pos[2]))


    def pot_energy(self) -> int:
        return abs(self.pos.x) + abs(self.pos.y) + abs(self.pos.z)

    def kin_energy(self) -> int:
        return abs(self.vel.x) + abs(self.vel.y) + abs(self.vel.z)

    def energy(self) -> int:
        return self.pot_energy() * self.kin_energy()

    def __eq__(self, b):
        return self.pos == b.pos and self.vel == b.vel

def solution():
    with open("input", "r") as f:
        inp = [x.strip() for x in f.readlines()]

    moons = []

    for line in inp:
        pos = line[1:-1].split(", ")
        x, y, z = (int(x.split("=")[1]) for x in pos)
        moons.append(Moon(Vec3(x, y, z), Vec3(0, 0, 0)))

    # Part 1

    for x in range(1000):
        for i in moons:
            for j in moons:
                if i == j:
                    continue
                i.vel += i.gravity(j)

        for i in moons:
            i.pos += i.vel

    print(sum(x.energy() for x in moons))

    # Part 2

    def gcd3(a, b, c):
        return gcd(gcd(a, b), c)

    def lcm(denoms):
        return reduce(lambda a, b: a*b // gcd(a,b), denoms)

    out = subprocess.check_output(["make", "run"]).split()[-3:]
    print(lcm([int(x.decode("ascii")) for x in out]))


if __name__ == '__main__':
    solution()
 