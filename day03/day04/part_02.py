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


def only_two_adjacent_digits_are_the_same(s):
    i1 = iter(s)
    i2 = iter(s)
    next(i2)
    candidates = [
        a for a, b in zip(i1, i2) if a == b
    ]
    for i in candidates:
        if s.count(i) == 2:
            return True
    return False

assert only_two_adjacent_digits_are_the_same('112233')
assert only_two_adjacent_digits_are_the_same('223450')
assert only_two_adjacent_digits_are_the_same('111122')
assert only_two_adjacent_digits_are_the_same('123444') is False
assert only_two_adjacent_digits_are_the_same('111111') is False
assert only_two_adjacent_digits_are_the_same('123789') is False

counter = 0
for num in range(367479, 893698+1):
    s = str(num)
    assert(len(s) == 6)
    if digits_never_decrease(s) and only_two_adjacent_digits_are_the_same(s):
        counter += 1
        # print(s)

print(f'Solution for part 2 is: {counter}')
