from car_class import Car


def display(c):
    for car in c:
        print(car)


def cars_details(d):
    with open("car_records.txt", 'w') as file:
        for car in d:
            print(car, file=file)


def oldest(cars_list):
    car_years = [car.year for car in cars_list]
    oldest_year = min(car_years)
    oldest_cars = [car for car in cars_list if car.year == oldest_year]
    return oldest_cars


def main():
    car_1 = Car("Ford", "Mustang", 1966)
    car_2 = Car("Dodge", "Charger", 1969)
    car_3 = Car("Ferrari", "F40", 1992)
    cars = [car_1, car_2, car_3]
    display(cars)
    cars_details(cars)
    old = oldest(cars)
    print()
    display(old)


if __name__ == '__main__':
    main()
