#!/usr/bin/env python


def digits_never_decrease(s):
    i1 = iter(s)
    i2 = iter(s)
    next(i2)
    return all(
        a <= b for a, b in zip(i1, i2)
        )


assert digits_never_decrease('111123')
assert digits_never_decrease('135679')
assert digits_never_decrease('111111')
assert digits_never_decrease('223450') is False


def two_adjacent_digits_are_the_same(s):
    i1 = iter(s)
    i2 = iter(s)
    next(i2)
    return any(
        a == b for a, b in zip(i1, i2)
        )


assert two_adjacent_digits_are_the_same('111111')
assert two_adjacent_digits_are_the_same('223450')
assert two_adjacent_digits_are_the_same('123789') is False

counter = 0
for num in range(367479, 893698+1):
    s = str(num)
    assert(len(s) == 6)
    if digits_never_decrease(s) and two_adjacent_digits_are_the_same(s):
        counter += 1
        print(s)

print(f'Solution for part 1 is: {counter}')
