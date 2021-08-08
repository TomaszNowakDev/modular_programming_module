# class for a coordinate containing x and y, calculate and return the distance of the coordinate from the origin (0,0).
import math


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x = {self.x} and y = {self.y} and the distance from (0,0) is: {self.counting()}"

    def counting(self):
        return math.sqrt(self.y**2 + self.x**2)


def main():
    c1 = Coordinate(int(input("First coordinate -> ")), int(input("Second coordinate -> ")))
    print(c1)


if __name__ == '__main__':
    main()
