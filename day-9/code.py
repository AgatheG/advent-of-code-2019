from advcode.intcode import IntcodeBOOST

# TESTS
data_output_middle = [104,1125899906842624,99]
assert IntcodeBOOST(data_output_middle, True).run() == data_output_middle[1]

data_quine = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
assert IntcodeBOOST(list(data_quine), False, True).run() == data_quine

data_output_big_number = [1102,34915192,34915192,7,4,7,99,0]
assert len(str(IntcodeBOOST(data_output_big_number, True).run())) == 16

# PART 1
with open("input.txt", "r") as file:
    data = map(int, file.read().split(","))
print(IntcodeBOOST(data).run(1))

# PART 2
with open("input.txt", "r") as file:
    data = map(int, file.read().split(","))
print(IntcodeBOOST(data).run(2))
