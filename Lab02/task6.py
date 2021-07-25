# printing name
def card(name1, surname2):
    full_name = f"{surname2},{name1}"
    return full_name


name = input("What is your name? ")
surname = input("What is your surname? ")
screen = card(name, surname)
print(screen)
