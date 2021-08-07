class Dog:
    def __init__(self, n, a, b):
        self.name = n
        self.age = a
        self.breed = b

    def __str__(self):
        return f"{self.name} is a {self.breed} and is age {self.age} years."

    def age_in_human_years(self):
        return self.age * 7
