from argparse import ArgumentParser

# PART 1

parser = ArgumentParser()
parser.add_argument(
    "-f", "-file", default="input.txt", dest="file")
parser.add_argument(
    "-c1", "-check_1", type=int, dest="value_test_1")
parser.add_argument(
    "-c2", "-check_2", type=int, dest="value_test_2")
args = parser.parse_args()

with open(args.file, "r") as file:
    path_1, path_2 = map(lambda x: x.split(","), file.read().split("\n"))

def is_vertical(direction):
    return direction == "U" or direction == "D"

def is_backward(direction):
    return direction == "D" or direction == "L"

class VerticalLine(object):
    def __init__(self, abscissa, ordinates):
        self.abscissa = abscissa
        self.ordinates = ordinates

    def get_direction(self):
        return "VERTICAL"

    def crosses(self, other):
        if other.get_direction() == "VERTICAL":
            return False
        return min(self.ordinates) <= other.ordinate <= max(self.ordinates) \
            and min(other.abscissae) <= self.abscissa <= max(other.abscissae)

    def manhattan_dist(self, other):
        return abs(self.abscissa) + abs(other.ordinate)

class HorizontalLine(object):
    def __init__(self, ordinate, abscissae):
        self.ordinate = ordinate
        self.abscissae = abscissae

    def get_direction(self):
        return "HORIZONTAL"

    def crosses(self, other):
        if other.get_direction() == "HORIZONTAL":
            return False
        return min(other.ordinates) <= self.ordinate <= max(other.ordinates) \
            and min(self.abscissae) <= other.abscissa <= max(self.abscissae)

    def manhattan_dist(self, other):
        return abs(other.abscissa) + abs(self.ordinate)

def get_line(lines, vertical, backward, distance):
    if backward:
        direction = -1
    else:
        direction = 1
    if vertical:
        if lines:
            line_before = lines[-1]
            return VerticalLine(line_before.abscissae[1],
                [line_before.ordinate, line_before.ordinate + direction*distance])
        return VerticalLine(0, [0, direction*distance])
    if lines:
        line_before = lines[-1]
        return HorizontalLine(line_before.ordinates[1],
            [line_before.abscissa, line_before.abscissa + direction*distance])
    return HorizontalLine(0, [0, direction*distance])

def get_lines():
    lines_1 = []
    lines_2 = []
    for move in path_1:
        direction, distance = move[0], int(move[1:])
        move_is_vertical, move_is_backward = is_vertical(direction), is_backward(direction)
        lines_1.append(get_line(lines_1,move_is_vertical,move_is_backward,distance))
    for move in path_2:
        direction, distance = move[0], int(move[1:])
        move_is_vertical, move_is_backward = is_vertical(direction), is_backward(direction)
        lines_2.append(get_line(lines_2,move_is_vertical,move_is_backward,distance))
    return lines_1, lines_2

def find_smallest_dist(cost_function):
    lines_1, lines_2 = get_lines()
    min_dist = float("Inf")
    for line in lines_1:
        for other_line in lines_2:
            if line.crosses(other_line):
                dist = cost_function(line, other_line)
                if dist > 0 and dist < min_dist:
                    min_dist = dist
    return min_dist

manhattan = lambda line, other_line: line.manhattan_dist(other_line)
result = find_smallest_dist(manhattan)

if result < float("Inf"):
    print("Distance to closest intersection is " + str(result))
else:
    print("No intersection between the two paths")

if args.value_test_1 is not None:
    assert args.value_test_1 == result

# PART 2

class VerticalLineWithSteps(VerticalLine):
    def __init__(self, abscissa, ordinates, distance, steps=0):
        super(VerticalLineWithSteps, self).__init__(abscissa, ordinates)
        self.steps = steps
        self.distance = distance

    def nr_steps_to_intersection(self, other):
        return abs(other.ordinate - self.ordinates[0])

    def step_distance(self, other):
        return self.steps + other.steps + self.nr_steps_to_intersection(other) + other.nr_steps_to_intersection(self)

class HorizontalLineWithSteps(HorizontalLine):
    def __init__(self, ordinate, abscissae, distance, steps=0):
        super(HorizontalLineWithSteps, self).__init__(ordinate, abscissae)
        self.steps = steps
        self.distance = distance

    def nr_steps_to_intersection(self, other):
        return abs(other.abscissa - self.abscissae[0])

    def step_distance(self, other):
        return self.steps + other.steps + self.nr_steps_to_intersection(other) + other.nr_steps_to_intersection(self)

def get_line(lines, vertical, backward, distance):
    if backward:
        direction = -1
    else:
        direction = 1
    if vertical:
        if lines:
            line_before = lines[-1]
            return VerticalLineWithSteps(line_before.abscissae[1],
                                        [line_before.ordinate, line_before.ordinate + direction*distance],
                                        distance,
                                        line_before.steps + line_before.distance)
        return VerticalLineWithSteps(0, [0, direction*distance], distance)
    if lines:
        line_before = lines[-1]
        return HorizontalLineWithSteps(line_before.ordinates[1],
                                    [line_before.abscissa, line_before.abscissa + direction*distance],
                                    distance,
                                    line_before.steps + line_before.distance)
    return HorizontalLineWithSteps(0, [0, direction*distance], distance)

step = lambda line, other_line: line.step_distance(other_line)
result = find_smallest_dist(step)

if result < float("Inf"):
    print("Distance to closest intersection (in steps) is " + str(result))
else:
    print("No intersection between the two paths")

if args.value_test_2 is not None:
    assert args.value_test_2 == result
