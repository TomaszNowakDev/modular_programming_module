class Book:
    def __init__(self, isbn, title, author, price):
        self.ISBN = isbn
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"IBSN = {self.ISBN}, Title = {self.title}, Author = {self.author}, Price = {self.price}"


def main():
    with open("books.txt") as connection:
        lines = connection.readlines()
        books = []
        for line in lines:
            split_line = line.split(",")
            ibsn = int(split_line[0])
            title = split_line[1]
            author = split_line[2]
            price = int(split_line[3])
            book = Book(ibsn, title, author, price)
            books.append(book)


if __name__ == '__main__':
    main()
