def read_list_of_words(file):
    connection = open(file)
    words = connection.readlines()
    connection.close()
    return [word.strip() for word in words]


def splitting(words):
    w = []
    for i in range(len(words)):
        list_words = words[i].split()
        for o in range(len(list_words)):
            if list_words[o] not in w:
                w.append(list_words[o])
    with open("some_words.txt", 'w') as file:
        for i in range(len(w)):
            print(w[i], file=file)


def main():
    list_of_words = read_list_of_words("string.txt")
    splitting(list_of_words)


if __name__ == '__main__':
    main()
