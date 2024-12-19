def run(a, b, c, pointer=0):
    global output, instructions
    while pointer < len(instructions):
        combo = combo_operand(instructions[pointer][1], a, b, c)
        literal = instructions[pointer][1]
        operator = instructions[pointer][0]
        '''
        print(f"pointer = {pointer}")
        print(f"instruction = {instructions[pointer]}")
        display(a, b, c, output)
        print()
        '''

        match operator:
            case 0: a = a // (2 ** combo)
            case 1: b = b ^ literal
            case 2: b = combo % 8
            case 3: pointer = literal - 1 if a != 0 else pointer
            case 4: b = b ^ c
            case 5: output.append(combo % 8)
            case 6: b = a // (2 ** combo)
            case 7: c = a // (2 ** combo)

        pointer += 1

    display(a, b, c)

def combo_operand(operand, a, b, c):
    if operand == 4:
        operand = a
    elif operand == 5:
        operand = b
    elif operand == 6:
        operand = c
    elif operand == 7:
        raise Exception("Reserved")
    return(operand)

def display(a, b, c):
    global output
    print(f"Register A: {a}\nRegister B: {b}\nRegister C: {c}\nOutput: {','.join(str(num) for num in output)}")

def step():
    global output, instructions
    count = 0
    while input() != "c":
        print(f"step = {count}")
        output = []
        run(count, 0, 0)
        print()
        count += 1

program = "2,4,1,5,7,5,0,3,4,1,1,6,5,5,3,0".split(',')
instructions = [(int(program[i]), int(program[i+1])) for i in range(0, len(program), 2)]
step()
'''
a = 47719761
b = 0
c = 0
output = []
run(a, b, c)
'''