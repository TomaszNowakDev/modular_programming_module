from functions import read_positive_integer, read_non_empty_string


def runner():
    name = read_non_empty_string("Enter name >>>")
    time = read_positive_integer("Enter race time >>>")
    return name, time


def t_shirt(t):
    if t < 25:
        return "Fast"
    else:
        return "Getting Faster"


def main():
    name, time = runner()
    fast = t_shirt(time)
    print(f'T-shirt for {name} : {fast}')


if __name__ == '__main__':
    main()
