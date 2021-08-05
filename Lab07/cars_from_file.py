from car_class import Car


def display(c):
    for car in c:
        print(car)


def cars_maker(cars, maker):
    return [car for car in cars if car.make == maker]


def do_not_show(cars, maker):
    return [car for car in cars if car.make != maker]


def main():
    with open("carsCSV.csv") as inputs:
        lines = inputs.readlines()

    cars = []
    for line in lines:
        split_line = line.split(",")
        make = split_line[0]
        model = split_line[1]
        year = int(split_line[2])
        car = Car(make, model, year)
        cars.append(car)
    display(cars)
    ford_cars = cars_maker(cars, "Ford")
    print("\nFord cars:")
    display(ford_cars)
    print("\nNot Fords: ")
    not_ford = do_not_show(cars, "Ford")
    display(not_ford)


if __name__ == '__main__':
    main()
