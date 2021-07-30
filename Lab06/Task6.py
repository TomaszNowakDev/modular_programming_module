# Tomasz Nowak
def read_list_of_words(file):
    connection = open(file)
    lines = connection.readlines()
    connection.close()
    names = []
    gamertags = []
    for i in range(len(lines)):
        split_line = lines[i].strip().split(',')
        names.append(split_line[0])
        gamertags.append(split_line[1])
    # gamertags = [tag.strip() for tag in gamertags]
    return names, gamertags


def display(name, gamertag):
    print(f"{'Name':20}{'Gamertag'}")
    print("==============================")
    for i in range(len(name)):
        print(f'{name[i]:20}{gamertag[i]}')


def average_length(x):
    total = 0
    for i in range(len(x)):
        total = total + len(x[i])
    aver = total / len(x)
    print(f'Average length of gamertag {aver} characters.')


def main():
    list_of_names, list_of_gametags = read_list_of_words("players.txt")
    display(list_of_names, list_of_gametags)
    average_length(list_of_gametags)


if __name__ == '__main__':
    main()
