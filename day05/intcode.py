#!/usr/bin/env python


import array

ADD = 1
MUL = 2
INP = 3
OUT = 4
HALT = 99


class Memory:

    def __init__(self, size=4006):
        self.size = size
        self.used = 0
        self.reset()

    def load(self, position):
        self.used = max(self.used, position)
        return self.core[position]

    def store(self, position, value):
        self.core[position] = value
        self.used = max(self.used, position)

    def reset(self):
        self.core = array.array('i', (0 for _ in range(self.size)))

    def dump(self):
        return ','.join(
            str(self.core[i])
            for i in range(0, self.used+1)
            )


class IntCode:

    def __init__(self, code=''):
        self.tron = False
        self.kernel = {
            ADD: self.add,
            MUL: self.mul,
            INP: self.inp,
            OUT: self.out,
        }
        self.mem = Memory()
        self.reset()
        if code:
            self.set_memory(code)

    def reset(self):
        self.pc = 0
        self.clock = 0
        self.mem.reset()

    def set_memory(self, code):
        self.mem.reset()
        for i, num in enumerate(code.split(',')):
            self.mem.store(i, int(num))

    def load(self, filename):
        with open(filename, 'r') as f:
            program = f.read().strip()
        self.set_memory(program)
        return self

    def dump(self):
        return (
            'IntCode DUMP:\n'
            f'PC: {self.pc}\n'
            f'TICKS: {self.clock}\n'
            f'MEMORY: {self.mem.dump()}\n'
        )

    def inc_pc(self, i=1):
        self.pc += i

    def get_opcode(self):
        opcode = self.mem.load(self.pc)
        if self.tron:
            print(f"TICK {self.clock}")
            print(f' - PC: {self.pc} | OP: {opcode}')
        return opcode

    def get_position_operand(self, position=1):
        addr_op = self.pc + position
        abs_pos = self.mem.load(addr_op)
        return self.mem.load(abs_pos)

    def get_inmediate_operand(self, position=1):
        addr_op = self.pc + position
        value = self.mem.load(addr_op)
        return value

    def store_absolute(self, addr_store, value):
        if self.tron:
            print(f" - STORE IN MEM[{addr_store}] VALUE: {value}")
        self.mem.store(addr_store, value)

    def store_relative(self, value, position=1):
        addr = self.mem.load(self.pc + position)
        if self.tron:
            print(f" - ADDR STORE: {addr} | VALUE: {value}")
        self.store_absolute(addr, value)

    def add(self):
        op1 = self.get_position_operand(1)
        op2 = self.get_position_operand(2)
        if self.tron:
            print(f" - OP1: {op1} + OP2: {op2} -> {op1 + op2}")
        self.store_relative(op1 + op2, 3)
        return 4

    def mul(self):
        op1 = self.get_position_operand(1)
        op2 = self.get_position_operand(2)
        if self.tron:
            print(f" - OP1: {op1} * OP2: {op2} -> {op1 * op2}")
        self.store_relative(op1 * op2, 3)
        return 4

    def inp(self):
        op = self.get_inmediate_operand(1)
        value = int(input('Enter value:'))
        self.store_absolute(op, value)
        return 2

    def out(self):
        op = self.get_inmediate_operand(1)
        value = self.mem.load(op)
        print(value)
        return 2

    def run(self):
        self.pc = 0
        while True:
            opcode = self.get_opcode()
            if opcode == HALT:
                break
            pc_delta = self.kernel[opcode]()
            self.inc_pc(pc_delta)
            self.clock += 1
        print(self.dump())
        return self
