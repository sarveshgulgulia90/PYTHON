import math

class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Coordinate):
            new_x = self.x + other.x
            new_y = self.y + other.y
            new_z = self.z + other.z
            return Coordinate(new_x, new_y, new_z)
        else:
            raise TypeError("Unsupported operand type for +: " + str(type(other)))

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def direction(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return Coordinate(0, 0, 0)  # Avoid division by zero
        return Coordinate(self.x / magnitude, self.y / magnitude, self.z / magnitude)

    def __str__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"

class Parallelepiped:
    def __init__(self, coordinate1, coordinate2, coordinate3):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2
        self.coordinate3 = coordinate3

    def volume(self):
        # Calculate the volume using the scalar triple product
        v1 = self.coordinate1
        v2 = self.coordinate2
        v3 = self.coordinate3

        scalar_triple_product = v1.x * (v2.y * v3.z - v3.y * v2.z) \
                               - v2.x * (v1.y * v3.z - v3.y * v1.z) \
                               + v3.x * (v1.y * v2.z - v2.y * v1.z)

        return abs(scalar_triple_product)



# Driver code for Coordinate class
point1 = Coordinate(1.0, 2.5, 3.5)
point2 = Coordinate(2.0, 3.0, 4.5)

sum_point = point1 + point2
magnitude = sum_point.magnitude()
direction = sum_point.direction()

print("Sum of points:", sum_point)
print("Magnitude:", magnitude)
print("Direction:", direction)

# Driver code for Parallelepiped class
parallelepiped_point1 = Coordinate(1, 0, 0)
parallelepiped_point2 = Coordinate(0, 2, 0)
parallelepiped_point3 = Coordinate(0, 0, 3)

parallelepiped_object = Parallelepiped(parallelepiped_point1, parallelepiped_point2, parallelepiped_point3)
volume = parallelepiped_object.volume()

print("Volume of Parallelepiped:", volume)
