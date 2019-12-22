#!/usr/bin/env python


ADD = 1
MUL = 2
HALT = 99


class IntCode:

    def __init__(self, code=''):
        self.tron = False
        self.kernel = {
            ADD: self.add,
            MUL: self.mul,
        }
        self.reset()
        if code:
            self.set_memory(code)

    def reset(self):
        self.pc = 0
        self.clock = 0
        self.memory = []

    def set_memory(self, code):
        self.memory = []
        for num in code.split(','):
            self.memory.append(int(num))

    def load(self, filename):
        with open(filename, 'r') as f:
            program = f.read().strip()
        self.set_memory(program)
        return self

    def dump(self):
        return ','.join(str(i) for i in self.memory)

    def inc_pc(self):
        self.pc += 4

    def get_opcode(self):
        if self.tron:
            print(f"TICK {self.clock}")
            print(f' - PC: {self.pc} | OP: {opcode}')
        return self.memory[self.pc]

    def get_operands(self):
        addr_op1 = self.memory[self.pc+1]
        addr_op2 = self.memory[self.pc+2]
        return self.memory[addr_op1], self.memory[addr_op2]

    def store_result(self, value):
        addr_store = self.memory[self.pc+3]
        if self.tron:
            print(f" - ADDR STORE: {addr_store} | VALUE: {value}")
        self.memory[addr_store] = value

    def add(self):
        op1, op2 = self.get_operands()
        if self.tron:
            print(f" - OP1: {op1} + OP2: {op2} -> {op1 + op2}")
        self.store_result(op1 + op2)

    def mul(self):
        op1, op2 = self.get_operands()
        if self.tron:
            print(f" - OP1: {op1} * OP2: {op2} -> {op1 * op2}")
        self.store_result(op1 * op2)

    def run(self):
        self.pc = 0
        while True:
            opcode = self.get_opcode()
            if opcode == HALT:
                break
            self.kernel[opcode]()
            self.inc_pc()
            self.clock += 1
        return self
