from my_classes import Fraction


def main():
    f1 = Fraction(3, 4)
    print(f1, '=', f1.decimal())
    print(f1.__dict__)  # checking components of the object.
    f2 = Fraction(7, 10)
    print(f2, '=', f2.decimal())
    print(f2.__dict__)


if __name__ == '__main__':
    main()
