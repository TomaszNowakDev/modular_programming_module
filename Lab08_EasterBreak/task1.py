from matplotlib import pyplot


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


def oldest_person(hum):
    ages = [h.age for h in hum]
    names = [name.name for name in hum]
    old_age = max(ages)
    print(f"Oldest person is/are: ")
    for i in range(len(ages)):
        if ages[i] == old_age:
            print(f"\t{names[i]}")


def youngest_person(hum):
    ages = [h.age for h in hum]
    names = [name.name for name in hum]
    young = min(ages)
    print(f"Youngest person is/are: ")
    for i in range(len(ages)):
        if ages[i] == young:
            print(f"\t{names[i]}")


def children(hum):
    kids = [kid.name for kid in hum if kid.age < 18]
    print(f"Children under 18: ")
    return kids


def pensioners_list(hum):
    pensioners = [per.name for per in hum if per.age >= 65]
    print(f"Pensioners:")
    return pensioners


def working_age(hum):
    workers = [w.name for w in hum if 18 <= w.age < 65]
    print(f"People in working age: ")
    return workers


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

    oldest_person(humans)
    youngest_person(humans)
    kids = children(humans)
    display(kids)
    print()

    pensioners = pensioners_list(humans)
    display(pensioners)
    print()
    workers = working_age(humans)
    display(workers)

    age_groups = ['Working age', 'Children', 'Pensioners']
    preferences = [len(workers), len(kids), len(pensioners)]
    fig, ax = pyplot.subplots()
    ax.pie(preferences, labels=age_groups, autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    pyplot.show()


if __name__ == '__main__':
    main()
