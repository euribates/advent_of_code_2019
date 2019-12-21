#!/usr/bin/env python


def calc_fuel(mass):
    return max(0, (mass // 3) - 2)


def get_total_fuel(mass):
    fuel_mass = calc_fuel(mass)
    delta = calc_fuel(fuel_mass)
    while delta > 0:
        fuel_mass += delta
        delta = calc_fuel(delta)
    return fuel_mass


assert calc_fuel(12) == 2
assert calc_fuel(14) == 2
assert calc_fuel(1969) == 654
assert calc_fuel(100756) == 33583

assert get_total_fuel(14) == 2
assert get_total_fuel(1969) == 966
assert get_total_fuel(100756) == 50346

acc = 0
for line in open('input', 'r'):
    acc += get_total_fuel(int(line.strip()))

print(f'Solution of second part is: {acc}')

