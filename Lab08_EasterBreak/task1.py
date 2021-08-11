class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"


def display(hum):
    for h in hum:
        print(h)


def average(hum):
    y = [h.age for h in hum]
    x = sum(y) / len(y)
    return x


def main():
    with open("people.cvs") as connection:
        lines = connection.readlines()
        humans = []
        for line in lines:
            split_line = line.split(",")
            name = split_line[0]
            age = int(split_line[1])
            people = People(name, age)
            humans.append(people)

    average_result = average(humans)
    print(f"Average age is: {average_result:.2f} years.")


if __name__ == '__main__':
    main()
