from math import pi


class Fraction:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def decimal(self):
        return self.numerator/self.denominator


class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __str__(self):
        return f"Height = {self.height} and width = {self.width}"

    def area(self):
        return self.width * self.height

    def circumference(self):
        return (self.width + self.height) * 2


class Circle:
    def __init__(self, r):
        self.radius = r

    def __str__(self):
        return f"Radius = {self.radius}"

    def area(self):
        return pi * self.radius ** 2

    def circumference(self):
        return 2 * pi * self.radius


