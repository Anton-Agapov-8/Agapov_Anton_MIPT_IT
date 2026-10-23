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

    def __str__(self):
        return '{' + f'{self.x}, {self.y}, {self.z}' + '}'


v1 = Vector(1, 2, 3)
v2 = Vector(2, 5, 4)
print(v1 + v2)
print(v1 * v2)
print(v1 * 4)
