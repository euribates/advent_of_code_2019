#!/usr/bin/env python

from intcode import IntCode

ic = IntCode().load('input')
ic.memory[1] = 12
ic.memory[2] = 2
ic.run()
solution = ic.memory[0]
print(f"Solution of first part is: {solution}")
