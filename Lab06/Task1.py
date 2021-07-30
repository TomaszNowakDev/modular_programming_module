# Tomasz Nowak
def read_list_of_words(file):
    connection = open(file)
    words = connection.readlines()
    connection.close()
    return [word.strip() for word in words]


def sort_list(x):
    y = sorted(x)
    return y


def saving(x):
    with open("sorted.txt", 'a') as file:
        for i in range(len(x)):
            print(x[i], file=file)


def main():
    list_of_words = read_list_of_words("words.txt")
    sorting = sort_list(list_of_words)
    saving(sorting)
    print(list_of_words)
    print(sorting)
    an = []
    for i in range(len(sorting)):
        if "an" in sorting[i]:
            an.append(sorting[i])
    print(an)


if __name__ == '__main__':
    main()
