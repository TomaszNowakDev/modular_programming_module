from car_class import Car


def display(c):
    for car in c:
        print(car)


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


if __name__ == '__main__':
    main()
