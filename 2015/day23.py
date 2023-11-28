with open('day23.txt', 'r') as f:
    instructions = f.read().strip().split('\n')
    instructions = [i.split() for i in instructions]
    
registers = {'a' : 0, 'b' : 0} # change a to 1 for part 2

inst = 0
get_num = lambda val : int(val[1:]) * (1 if val[0] == '+' else -1)

while True:
    if inst >= len(instructions):
        break
    i = instructions[inst]
    opcode = i[0]
    last = i[-1]

    match opcode:
        case 'hlf':
            registers[last] //= 2
        case 'tpl':
            registers[last] *= 3
        case 'inc':
            registers[last] += 1
        case 'jmp':
            inst += get_num(last)
            continue
        case 'jie':
            inst += get_num(last) if registers[i[1][0]] % 2 == 0 else 1
            continue
        case 'jio':
            inst += get_num(last) if registers[i[1][0]] == 1 else 1
            continue

    inst += 1

print(registers['b'])
