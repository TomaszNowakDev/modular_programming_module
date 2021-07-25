# Simple converter between kilometres, meters, feet and inches.
MAIN_MENU = "1. Convert to kilometres\n2. Convert to feet\n3. Convert to inches\n4. Quit\n==>"


def convert(ch, dis):
    if ch == 1:
        print(f"{dis} meters is {dis * 0.001} km.\n")
    elif ch == 2:
        print(f"{dis} meters is {dis * 3.28084} feet.\n")
    elif ch == 3:
        print(f"{dis} meters is {dis * 39.3701} inches.\n")


def main():
    main_choice = int(input(MAIN_MENU))
    while main_choice != 4:
        distance = float(input("Distance in meters? "))
        convert(main_choice, distance)
        main_choice = int(input(MAIN_MENU))


main()
