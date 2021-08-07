from my_classes1 import Dog


def main():
    connection = open("dogsList.csv")
    lines = connection.readlines()
    connection.close()
    dogs = []
    for line in lines:
        split_line = line.split(',')
        name = split_line[0]
        age = int(split_line[1])
        breed = split_line[2].strip()
        dog = Dog(name, age, breed)
        dogs.append(dog)

    for dog in dogs:
        print(dog)

    ages_list = [dog.age for dog in dogs]
    average = sum(ages_list) / len(ages_list)
    print(f'{average:.2f}')
    oldest = max(ages_list)
    print("The oldest dog/dogs is/are", oldest, "years old, name/names:")
    for dog in dogs:
        if dog.age == oldest:
            print(dog.name)


if __name__ == '__main__':
    main()
