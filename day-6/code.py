from collections import deque

class SpaceObject(object):
    def __init__(self, orbited=None):
        self.orbiters = set()
        self.orbited = orbited
        self.distance_to_com = 0

class Map(object):
    def __init__(self, orbits):
        self.objects = {}
        self._build_map(orbits)
        self.orbits = 0
        self._find_orbits()

    def _build_map(self, orbits):
        for orbit in orbits:
            orbited, orbiter = orbit.split(")")
            if self.objects.get(orbiter) is None:
                self.objects[orbiter] = SpaceObject(orbited)
            else:
                self.objects[orbiter].orbited = orbited
            if self.objects.get(orbited) is None:
                self.objects[orbited] = SpaceObject()
            self.objects[orbited].orbiters.add(orbiter)

    def _find_orbits(self):
        to_visit = deque(self.objects.get("COM").orbiters)
        while to_visit:
            current_sp_obj = self.objects[to_visit.popleft()]
            current_sp_obj.distance_to_com = self.objects[current_sp_obj.orbited].distance_to_com + 1
            self.orbits += current_sp_obj.distance_to_com
            to_visit += current_sp_obj.orbiters

    #PART 2
    def find_shortest_distance(self):
        from_me = self.objects["YOU"].orbited
        from_santa = self.objects["SAN"].orbited
        dist = 0
        while from_me != from_santa:
            space_object_in_my_path, space_object_in_santa_path = self.objects[from_me], self.objects[from_santa]
            if space_object_in_my_path.distance_to_com < space_object_in_santa_path.distance_to_com:
                from_santa = space_object_in_santa_path.orbited
            else:
                from_me = space_object_in_my_path.orbited
            dist += 1
        return dist

# TESTS

with open("test.txt", "r") as file:
    orbits = file.read().split("\n")

m = Map(orbits[:11])
assert m.orbits == 42
m = Map(orbits)
assert m.find_shortest_distance() == 4

with open("input.txt", "r") as file:
    orbits = file.read().split("\n")

m = Map(orbits)
print("Number of orbits is " + str(m.orbits))
print("The shortest distance is " + str(m.find_shortest_distance()))
