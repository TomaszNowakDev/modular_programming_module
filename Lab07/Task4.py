from math import pi


class Cylinder:
    def __init__(self, h, r):
        self.height = h
        self.radius = r

    def __str__(self):
        return f"Height = {self.height}, Radius = {self.radius}"

    def surface_area(self):
        return f"Area of the square is {(2 * pi * self.radius * self.height) + 2 * pi * self.radius**2}."


def main():
    c1 = Cylinder(5, 3)
    c2 = Cylinder(3, 4)
    print(c1)
    print(c1.surface_area())
    print(c2)
    print(c2.surface_area())


if __name__ == '__main__':
    main()
