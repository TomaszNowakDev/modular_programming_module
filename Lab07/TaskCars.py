from car_class import Car


def main():
    car_1 = Car("Ford", "Mustang", 1966)
    car_2 = Car("Dodge", "Charger", 1969)
    car_3 = Car("Ferrari", "F40", 1992)
    car_4 = Car(input("Enter made of your car "), input("What model is it? "), int(input("What year is it? ")))
    print(car_1, car_1.nct())
    print(car_2, car_2.nct())
    print(car_3, car_3.nct())
    print(car_4, car_4.nct())


if __name__ == '__main__':
    main()
