#!/usr/bin/env python

def calc_fuel(mass):
    return (mass // 3) - 2

assert calc_fuel(12) == 2
assert calc_fuel(14) == 2
assert calc_fuel(1969) == 654
assert calc_fuel(100756) == 33583

acc = 0
for line in open('input', 'r'):
    acc += calc_fuel(int(line.strip()))

print(f'Solution of first day is: {acc}')

