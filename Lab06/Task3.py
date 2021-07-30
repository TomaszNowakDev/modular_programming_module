# Tomasz Nowak
def read_lists(file):
    connection = open(file)
    lines = connection.readlines()
    connection.close()
    fruit = []
    stock = []
    for i in range(len(lines)):
        split_line = lines[i].split(',')
        fruit.append(split_line[0])
        stock.append(int(split_line[1]))
    return fruit, stock


def display(sto, fru):
    print(f"{'Fruit':20}{'Stock'}")
    print("========================")
    for i in range(len(fru)):
        print(f'{fru[i]:20}{sto[i]}')


def most_in_stock(fruits, stock):
    most = max(stock)
    x = stock.index(most)
    print(f'Most in stock {fruits[x]}: {most}')


def main():
    list_of_fruits, list_of_stock = read_lists("fruits.txt")
    display(list_of_stock, list_of_fruits)
    most_in_stock(list_of_fruits, list_of_stock)


if __name__ == '__main__':
    main()
