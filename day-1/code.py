# PART 1

def fuel(mass):
    return max(mass/3 - 2, 0)

with open("input.txt", "r") as file:
    mass_list = file.read().split("\n")

print(sum(fuel(int(mass)) for mass in mass_list))

#PART 2

def fuel_requirement(mass):
    current_fuel = fuel(mass)
    total_fuel = current_fuel
    while current_fuel > 0:
        current_fuel = fuel(current_fuel)
        total_fuel += current_fuel
    return total_fuel

print(sum(fuel_requirement(int(mass)) for mass in mass_list))
