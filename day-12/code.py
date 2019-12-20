NR_MOONS = 4

class Moon(object):
    NR_AXIS = 3
    def __init__(self, positions):
        self.positions = [int(position.split("=")[1]) for position in positions]
        self.velocities = [0,0,0]

    def apply_gravity(self, other):
        for axis in range(self.NR_AXIS):
            if self.positions[axis] < other.positions[axis]:
                self.velocities[axis] += 1
                other.velocities[axis] -= 1
            elif self.positions[axis] > other.positions[axis]:
                self.velocities[axis] -= 1
                other.velocities[axis] += 1

    def apply_velocity(self):
        for axis, velocity in enumerate(self.velocities):
            self.positions[axis] += velocity

    def _get_kinetic_energy(self):
        return sum(abs(pos) for pos in self.positions)

    def _get_potential_energy(self):
        return sum(abs(velocity) for velocity in self.velocities)

    def get_total_energy(self):
        return self._get_kinetic_energy() * self._get_potential_energy()

with open("test.txt", "r") as file:
    unparsed_positions = file.read().split("\n")

moons = []
for unparsed_position in unparsed_positions:
    moons.append(Moon(unparsed_position[1:-1].split(", ")))    

def simulate_one_step():
    for index_moon in range(NR_MOONS):
        for index_other_moon in range(index_moon+1, NR_MOONS):
            moons[index_moon].apply_gravity(moons[index_other_moon])
        moons[index_moon].apply_velocity()

for i in range(100):
    simulate_one_step()

print(sum(m.get_total_energy() for m in moons))
