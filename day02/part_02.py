#!/usr/bin/env python

from intcode import IntCode

with open('input', 'r') as f:
    program = f.read().strip()

def problem_space():
    for verb in range(100):
        for noun in range(100):
            yield verb, noun

ic = IntCode()
for verb, noun in problem_space():
    ic.reset()
    ic.set_memory(program)
    ic.memory[1] = noun
    ic.memory[2] = verb
    ic.run()
    m0 = ic.memory[0]
    if m0 == 19690720:
        print(f"verb is: {verb}")
        print(f"noun is: {noun}")
        solution = 100 * noun + verb
        print(f"Solution of second part is: {solution}")
        break
