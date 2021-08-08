class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def __str__(self):
        return f"Height is {self.height} and the base is {self.base} area is {self.area()}."

    def area(self):
        area = .5 * self.base * self.height
        return area


def main():
    t1 = Triangle(5, 3)
    print(t1)


if __name__ == '__main__':
    main()
