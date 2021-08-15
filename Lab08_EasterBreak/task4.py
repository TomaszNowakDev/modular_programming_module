from functions import read_positive_integer, read_non_empty_string


def runner():
    name = read_non_empty_string("Enter name >>>")
    time = read_positive_integer("Enter race time >>>")
    return name, time


def main():
    name, time = runner()


if __name__ == '__main__':
    main()
