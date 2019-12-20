from itertools import permutations
from advcode.intcode import IntcodeTESTThermalControl as Intcode

def get_prgm(file="input.txt"):
    with open(file, "r") as file:
        return map(int, file.read().split(","))

# PART 1
best_perm = []
max_output = 0
for perm in permutations([0,1,2,3,4]):
    output_a = Intcode(get_prgm()).run(perm[0], 0)
    output_b = Intcode(get_prgm()).run(perm[1], output_a)
    output_c = Intcode(get_prgm()).run(perm[2], output_b)
    output_d = Intcode(get_prgm()).run(perm[3], output_c)
    output = Intcode(get_prgm()).run(perm[4], output_d)
    if output > max_output:
        best_perm = perm
        max_output = output

print("Maximum output is " + str(max_output) + " obtained with combination " + str(best_perm))
