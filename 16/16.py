import re

samples = []
program = []

with open('input.txt') as file:
    line = file.readline()
    while line:
        if line == '\n':
            pass
        elif 'Before' in line:
            sample = []
            line = re.findall(r"[-\d']+", line)
            line = list(map(int, line))
            sample += [line]
            line = file.readline()
            line = re.findall(r"[-\d']+", line)
            line = list(map(int, line))
            sample += [line]
            line = file.readline()
            line = re.findall(r"[-\d']+", line)
            line = list(map(int, line))
            sample += [line]
            samples += [sample]
        else:
            line = re.findall(r"[-\d']+", line)
            line = list(map(int, line))
            program += [line]
        line = file.readline()

def addr(r, a, b, c):
    registers = r.copy()
    registers[c] = registers[a] + registers[b]
    return registers

def addi(r, a, b, c):
    registers = r.copy()
    registers[c] = registers[a] + b
    return registers

def mulr(r, a, b, c):
    registers = r.copy()
    registers[c] = registers[a] * registers[b]
    return registers

def muli(r, a, b, c):
    registers = r.copy()
    registers[c] = registers[a] * b
    return registers

def banr(r, a, b, c):
    registers = r.copy()
    registers[c] = registers[a] & registers[b]
    return registers

def bani(r, a, b, c):
    registers = r.copy()
    registers[c] = registers[a] & b
    return registers

def borr(r, a, b, c):
    registers = r.copy()
    registers[c] = registers[a] | registers[b]
    return registers

def bori(r, a, b, c):
    registers = r.copy()
    registers[c] = registers[a] | b
    return registers

def setr(r, a, b, c):
    registers = r.copy()
    registers[c] = registers[a]
    return registers

def seti(r, a, b, c):
    registers = r.copy()
    registers[c] = a
    return registers

def gtir(r, a, b, c):
    registers = r.copy()
    registers[c] = 1 if a > registers[b] else 0
    return registers

def gtri(r, a, b, c):
    registers = r.copy()
    registers[c] = 1 if registers[a] > b else 0
    return registers

def gtrr(r, a, b, c):
    registers = r.copy()
    registers[c] = 1 if registers[a] > registers[b] else 0
    return registers

def eqir(r, a, b, c):
    registers = r.copy()
    registers[c] = 1 if a == registers[b] else 0
    return registers

def eqri(r, a, b, c):
    registers = r.copy()
    registers[c] = 1 if registers[a] == b else 0
    return registers

def eqrr(r, a, b, c):
    registers = r.copy()
    registers[c] = 1 if registers[a] == registers[b] else 0
    return registers

opcodes = {addr, addi, mulr, muli, banr, bani, borr, bori, \
           setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr}

opcodes_dict = {}
not_opcodes_dict = {}

for op in opcodes:
    opcodes_dict[op] = []
    not_opcodes_dict[op] = []

behave = 0
for sample in samples:
    behave_sample = 0
    for op in opcodes:
        r = sample[0]
        opcode = sample[1][0]
        a = sample[1][1]
        b = sample[1][2]
        c = sample[1][3]
        after = sample[2]
        try:
            after_op = op(r, a, b, c)
            if after_op == after:
                behave_sample += 1
                if opcode not in not_opcodes_dict[op] and opcode not in opcodes_dict[op]:
                    opcodes_dict[op] += [opcode]
            else:
                if opcode not in not_opcodes_dict[op]:
                    not_opcodes_dict[op] += opcode
                if opcode in opcodes_dict[op]:
                    opcodes_dict[op].remove(opcode)
        except:
            if opcode not in not_opcodes_dict[op]:
                not_opcodes_dict[op] += [opcode]
            if opcode in opcodes_dict[op]:
                opcodes_dict[op].remove(opcode)
    if behave_sample >= 3:
        behave += 1

print(f'part 1: {behave}')

# filter opcodes
for op in opcodes_dict:
    for op in opcodes_dict:
        if len(opcodes_dict[op]) == 1:
            for op2 in opcodes_dict:
                if op != op2:
                    if opcodes_dict[op][0] in opcodes_dict[op2]:
                        opcodes_dict[op2].remove(opcodes_dict[op][0])

opcodes_function = {v[0]: k for k, v in opcodes_dict.items()}

registers = [0, 0, 0, 0]
for statement in program:
    opcode = statement[0]
    a = statement[1]
    b = statement[2]
    c = statement[3]
    registers = opcodes_function[opcode](registers, a, b, c)

print(f'part 2: {registers[0]}')
