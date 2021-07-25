# Program measures distance between two points in Cartesian
def distance(x1, y1, x2, y2):
    import math
    x = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return x


def main():
    print("=======================================================")
    print("Let's measure distance between two points in Cartesian!")
    print("=======================================================\n")
    point1 = int(input("The coordinates of the first point, length >"))
    point2 = int(input("The coordinates of the first point,  height>"))
    point3 = int(input("The coordinates of the second point, length >"))
    point4 = int(input("The coordinates of the second point,  height>"))

    result = distance(point1, point2, point3, point4)
    print(f"{result} is the distance between this two points.")


main()
