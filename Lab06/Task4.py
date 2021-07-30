# Tomasz Nowak
def read_lists(file):
    connection = open(file)
    lines = connection.readlines()
    connection.close()
    fruit = []
    stock = []
    price = []
    for i in range(len(lines)):
        split_line = lines[i].split(',')
        fruit.append(split_line[0])
        stock.append(int(split_line[1]))
        price.append(float(split_line[2]))
    return fruit, stock, price


def display(sto, fru, pri):
    print(f"{'Fruit':20}{'Stock':10}{'Price'}")
    print("====================================")
    for i in range(len(fru)):
        print(f'{fru[i]:20}{sto[i]:<10}{pri[i]}')


def most_in_stock(fruits, stock):
    most = max(stock)
    x = stock.index(most)
    print(f'Most in stock {fruits[x]}: {most}')


def total(pri, sto):
    total_value = 0
    for i in range(len(pri)):
        total_value = total_value + (pri[i] * sto[i])
    print(f'Total value of stock: {total_value}')


def main():
    list_of_fruits, list_of_stock, list_of_prices = read_lists("fruits2.txt")
    display(list_of_stock, list_of_fruits, list_of_prices)
    most_in_stock(list_of_fruits, list_of_stock)
    total(list_of_prices, list_of_stock)


if __name__ == '__main__':
    main()
