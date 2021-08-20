# This program is calculating area of shapes
MENU = "Shapes:\n1. Square\n2. Rectangle\n3. Right-angled triangle\n4. Circle\n5. Quit"


def main():
    print(MENU)
    choice_main = input("==> ")

    while choice_main != 5:
        if choice_main == 1:
            print("1. Square")

        elif choice_main == 2:
            print("2. Rectangle")

        elif choice_main == 3:
            print("3. Right-angled triangle")

        elif choice_main == 4:
            print("4. Circle")

        print(MENU)
        choice_main = input("==> ")
    print("Thank you, goodbye.")


if __name__ == '__main__':
    main()
