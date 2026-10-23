class Vector:
    def __init__(self, xyz):
        x = xyz[0]
        y = xyz[1]
        z = xyz[2]
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
            return Vector((self.x + other.x, self.y + other.y, self.z + other.z))

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector((self.x - other.x, self.y - other.y, self.z - other.z))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if isinstance(other, (int, float)) and not isinstance(other, bool):
            return Vector((self.x * other, self.y * other, self.z * other))

    def __str__(self):
        return '{' + f'{self.x}, {self.y}, {self.z}' + '}'


points = ((1, 2, 5), (4, 7, 8), (10, 12, 8))
summvec = Vector((0, 0, 0))
for point in points:
    summvec = summvec + Vector(point)
center = summvec * (1 / len(points))
print(center)
