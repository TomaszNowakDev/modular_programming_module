from math import pi


class Circle:
    def __init__(self, r):
        self.radius = r

    def __str__(self):
        return f"Radius = {self.radius}"

    def area(self):
        return pi * self.radius ** 2

    def circumference(self):
        return 2 * pi * self.radius


def main():
    c1 = Circle(5)
    c2 = Circle(4.6)
    print(f'{c1}, Area = {c1.area():.4f}, Circumference = {c1.circumference():.4f}')
    print(c2, ", Area = ", c2.area(), ", Circumference = ", c2.circumference())


if __name__ == '__main__':
    main()
