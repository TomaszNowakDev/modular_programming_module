class Car:
    def __init__(self, mk, md, y):
        self.make = mk
        self.model = md
        self.year = y

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

    def nct(self):
        return self.year + 4
