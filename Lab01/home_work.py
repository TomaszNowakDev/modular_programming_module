def countdown(x, y):
    for x in range(x, y - 1, -1):
        print(x, end=" ")
        if x == 0:
            print("Blast Off!")
            break
    else:
        print('Mission Aborted!')


def main():
    countdown(int(input("Enter the starting number -> ")), int(input("Enter the number to stop at ->")))


if __name__ == '__main__':
    main()
