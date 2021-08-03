class Square:
    def __init__(self, s):
        self.side = s

    def __str__(self):
        return f"Side = {self.side}"

    def area(self):
        return f"Area of the square is {self.side * self.side}."

    def circumference(self):
        return f"Circumference of the square id {4 * self.side}."


def main():
    s1 = Square(5)
    s2 = Square(7.6)
    print(s1)
    print(s1.area(), s1.circumference())
    print(s2)
    print(s2.area(), s1.circumference())


if __name__ == '__main__':
    main()
