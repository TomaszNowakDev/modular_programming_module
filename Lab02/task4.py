# this program indicates a larger number
def what_bigger(a, b):
    if a > b:
        x = a
    else:
        x = b
    return x


def main():
    num = what_bigger((int(input("Enter first number ==> "))), int(input("Enter second number ==> ")))
    print(f"Bigger is {num}.")


main()
