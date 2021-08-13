class Book:
    def __init__(self, isbn, title, author, price):
        self.ISBN = isbn
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"IBSN = {self.ISBN}, Title = {self.title}, Author = {self.author}, Price = {self.price}"


def cheapest(books_list):
    prices = [p.price for p in books_list]
    cheap = min(prices)
    titles = [t.title for t in books_list]
    authors = [a.author for a in books_list]
    print(f"Cheapest book(s) cost €{cheap}:")
    for i in range(len(books_list)):
        if books_list[i].price == cheap:
            print(f"{books_list[i].title} writen by {books_list[i].author}")


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

    cheapest(books)


if __name__ == '__main__':
    main()
