# This program is calculating area of shapes
MENU = "Shapes:\n1. Square\n2. Rectangle\n3. Right-angled triangle\n4. Circle\n5. Quit"


def validation_for_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                return user_input
        except ValueError:
            print("Whole positive numbers only please.")


def square():
    square_side = validation_for_input("What is the side length of the square? ")
    return square_side ** 2


def validation_for_menu(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if 0 < choice <= 5:
                break
            else:
                print("Choose one of the options from 1 to 5.")
        except ValueError:
            print("Numbers only please!")
    return choice


def main():
    print(MENU)
    choice_main = validation_for_menu("==> ")

    while choice_main != 5:
        if choice_main == 1:
            print("=====================")
            print("1. Square")
            print("=====================")
            square_area = square()
            print(f"Area of the square is {square_area}.")

        elif choice_main == 2:
            print("2. Rectangle")

        elif choice_main == 3:
            print("3. Right-angled triangle")

        elif choice_main == 4:
            print("4. Circle")
        print(MENU)
        choice_main = validation_for_menu("==> ")
    print("Thank you, goodbye.")


if __name__ == '__main__':
    main()
