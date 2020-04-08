# make a class LatLon that can be passed parameters `lat` and `lon` to the constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f'{self.lat}, {self.lon}'

# make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the constructor
# it should inherit from LatLon
# look up the `super` method

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return f'{self.name}, {self.lat}, {self.lon}'

# make a class Geocache that can be passed parameters `name`, `difficulty`, `size`, `lat`, and `lon` to the constructor
# what should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f'{self.name}, diff {self.difficulty}, {self.lat}, {self.lon}'

# make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint('Catacombs', 41.70505, -121.51521)

# without changing the following line, how can you make it print into something more human-readable?
# hint: Look up the 'object.__str__' method

print(str(waypoint))

# make a new geocache 'Newberry Views', diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache('Newberry Views', 1.5, 2, 44.052137, -121.41556)

# print it

print(geocache)