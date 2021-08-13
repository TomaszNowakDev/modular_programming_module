class Book:
    def __init__(self, isbn, title, author, price):
        self.ISBN = isbn
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"IBSN = {self.ISBN}, Title = {self.title}, Author = {self.author}, Price = {self.price}"

