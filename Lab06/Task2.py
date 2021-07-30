# Tomasz Nowak
def read_list_of_prices(file):
    connection = open(file)
    prices = connection.readlines()
    connection.close()
    return [int(price.strip()) for price in prices]


def high(x):
    return max(x)


def cheap(x):
    return min(x)


def average(houses):
    aver = sum(houses) / len(houses)
    return aver


def saving_into_a_file(x):
    y = sorted(x)
    y.reverse()
    with open("dearest_to_cheapest.txt", 'w') as file:
        for i in range(len(y)):
            print(y[i], file=file)


def main():
    house_prices_catch = read_list_of_prices("house_prices.txt")
    highest = high(house_prices_catch)
    cheapest = cheap(house_prices_catch)
    avr = average(house_prices_catch)
    saving_into_a_file(house_prices_catch)
    print(house_prices_catch)
    print(f'The most expensive house costs {highest}.')
    print(f'The cheapest house costs {cheapest}.')
    print(f'The average price of house is {avr}')


if __name__ == '__main__':
    main()
