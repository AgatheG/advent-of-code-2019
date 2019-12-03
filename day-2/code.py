# PART 1

def get_input():
    with open("input.txt", "r") as file:
        intcode_prgm = map(int, file.read().split(","))

    return intcode_prgm

intcode_prgm = get_input()
intcode_prgm[1] = 10
intcode_prgm[2] = 2

def run_intcode(prgm):
    index = 0
    while index < len(prgm)/4:
        opcode, left_param_idx, right_param_idx, output_idx = prgm[4*index], prgm[4*index+1], prgm[4*index+2], prgm[4*index+3]
        if opcode == 1:
            prgm[output_idx] = prgm[left_param_idx] + prgm[right_param_idx]
        elif opcode == 2:
            prgm[output_idx] = prgm[left_param_idx] * prgm[right_param_idx]
        elif opcode == 99:
            return prgm
        else:
            raise Exception("Wrong opcode")
        index += 1
    return prgm

print(run_intcode(intcode_prgm)[0])

# PART 2

for x in range(100):
    for y in range(100):
        new_input = get_input()
        new_input[1] = x
        new_input[2] = y

        if run_intcode(new_input)[0] == 19690720:
            print(100*x + y)
