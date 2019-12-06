class Intcode(object):
    class Opcode:
        ADD = 1
        MULT = 2
        STORE = 3
        OUTPUT = 4
        STOP = 99

    class Mode:
        POSITION = 0
        IMMEDIATE = 1

    def __init__(self, prgm):
        self.prgm = prgm
        self.pointer = 0

    def read_instruction(self, opcode, modes, diagnostic_input):
        if opcode == self.Opcode.STOP:
            return False
        if opcode == self.Opcode.OUTPUT:
            print(self.read_next(modes%10))
            self.inc()
            return True
        if opcode == self.Opcode.STORE:
            self.set_value(self.read_next(), diagnostic_input)
            self.inc()
            return True
        if opcode == self.Opcode.ADD:
            first = self.read_next(modes%10)
            modes /= 10
            second = self.read_next(modes%100)
            self.set_value(self.read_next(), first+second)
            self.inc()
            return True
        if opcode == self.Opcode.MULT:
            first = self.read_next(modes%10)
            modes /= 10
            second = self.read_next(modes%100)
            self.set_value(self.read_next(), first*second)
            self.inc()
            return True
        raise Exception("Opcode is invalid : " + str(opcode))

    def inc(self):
        self.pointer += 1

    def set_value(self, index, value):
        self.prgm[index] = value

    def get_current_value(self):
        return self.prgm[self.pointer]

    def read_next(self, mode=1):
        self.inc()
        if mode == self.Mode.POSITION:
            return self.prgm[self.get_current_value()]
        if mode == self.Mode.IMMEDIATE:
            return self.get_current_value()
        raise Exception("Mode is invalid : " + str(mode))

    def run(self, diagnostic_input):
        while self.pointer < len(self.prgm):
            opcode, mode = self.get_current_value()%100, self.get_current_value()/100
            if not self.read_instruction(opcode, mode, diagnostic_input):
                return self.prgm
        return self.prgm

with open("input.txt", "r") as file:
    prgm = map(int, file.read().split(","))

Intcode(prgm).run(input("Enter the ID of the system (ship's air conditioner unit) : "))

# PART 2

class IntcodeTESTThermalControl(Intcode):
    class OpcodeThermalControl:
        JUMP_IF_TRUE = 5
        JUMP_IF_FALSE = 6
        LESS_THAN = 7
        EQUALS = 8

    def read_instruction(self, opcode, modes, diagnostic_input):
        if opcode == self.OpcodeThermalControl.JUMP_IF_TRUE:
            to_test, modes = self.read_next(modes%10), modes / 10
            new_pointer = self.read_next(modes%100)
            if to_test != 0:
                self.pointer = new_pointer
            else:
                self.inc()
            return True
        if opcode == self.OpcodeThermalControl.JUMP_IF_FALSE:
            to_test, modes = self.read_next(modes%10), modes / 10
            new_pointer = self.read_next(modes%100)
            if to_test == 0:
                self.pointer = new_pointer
            else:
                self.inc()
            return True
        if opcode == self.OpcodeThermalControl.LESS_THAN:
            left, modes = self.read_next(modes%10), modes / 10
            right = self.read_next(modes%100)
            self.set_value(self.read_next(), 1 if left < right else 0)
            self.inc()
            return True
        if opcode == self.OpcodeThermalControl.EQUALS:
            left, modes = self.read_next(modes%10), modes/10
            right = self.read_next(modes%100)
            self.set_value(self.read_next(), 1 if left == right else 0)
            self.inc()
            return True
        return super(IntcodeTESTThermalControl, self).read_instruction(opcode, modes, diagnostic_input)

with open("input.txt", "r") as file:
    prgm = map(int, file.read().split(","))

IntcodeTESTThermalControl(prgm).run(input("Enter the ID of the system (ship's thermal radiator controller) : "))
