class Vector:
    def __init__(self, x, y, z):
        assert isinstance(x, (int, float)) and not isinstance(x, bool)
        assert isinstance(y, (int, float)) and not isinstance(y, bool)
        assert isinstance(z, (int, float)) and not isinstance(z, bool)
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if isinstance(other, (int, float)) and not isinstance(other, bool):
            return Vector(self.x * other, self.y * other, self.z * other)
        raise AssertionError

    def vector_mul(self, other):
        if isinstance(other, Vector):
            return Vector((self.y * other.z - self.z * other.y),
                          (self.x * other.z - self.z * other.x),
                          (self.x * other.y - self.y * other.x))
        raise AssertionError

    def __str__(self):
        return '{' + f'{self.x}, {self.y}, {self.z}' + '}'


points = ((1, 3, 7), (2, 5, 4), (13, 4, 1), (5, 4, 3))
vectors = []

for p1 in points:
    for p2 in points:
        if p1 != p2:
            vectors.append(Vector(p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]))

maxarea = 0
for vec in vectors:
    for vec2 in vectors:
        area = abs(vec.vector_mul(vec2))
        if area > maxarea:
            maxarea = area
print(maxarea / 2)
