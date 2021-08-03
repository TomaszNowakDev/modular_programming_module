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


def main():
    r1 = Rectangle(5, 7)
    r2 = Rectangle(4.5, 3)
    print(r1)
    print(r1.area(), r1.circumference())
    print(r2)
    print(r2.area(), r1.circumference())


if __name__ == '__main__':
    main()
