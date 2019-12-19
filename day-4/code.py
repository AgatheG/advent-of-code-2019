lower_bound = 347312
upper_bound = 805915

# PART 1
number = lower_bound
possible_codes = 0
while number <= upper_bound:
    number_split = map(int,str(number))
    previous_number = number_split[0]
    has_duplicate, proper_order = False, True
    for idx in range(1,6):
        current_number = number_split[idx]
        if current_number == previous_number:
            has_duplicate = True
        if current_number < previous_number:
            proper_order = False
            break
        previous_number = current_number
    if has_duplicate and proper_order:
        possible_codes += 1
    number += 1
print(str(possible_codes) + " different passwords meet the criteria")

# PART 2

from collections import Counter

number = lower_bound
possible_codes = 0
while number <= upper_bound:
    number_split = map(int,str(number))
    previous_number = number_split[0]
    has_pair, proper_order = False, True
    nr_duplicates = 0
    for idx in range(1,6):
        current_number = number_split[idx]
        if current_number < previous_number:
            proper_order = False
            break
        previous_number = current_number
    if proper_order and 2 in Counter(number_split).values():
        possible_codes += 1
    number += 1

print(str(possible_codes) + " different passwords meet the criteria")
