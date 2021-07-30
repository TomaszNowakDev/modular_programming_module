# Tomasz Nowak
def g_words(file):
    connection = open(file)
    words = connection.readlines()
    connection.close()
    x = [word.strip() for word in words]
    with open("g_words.txt", 'w') as file:
        print([w.strip() for w in x if w.startswith("g") or w.startswith("G")], file=file)


def main():
    g_words("Task7_words.txt")


if __name__ == '__main__':
    main()
