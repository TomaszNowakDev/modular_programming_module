def hair(x):
    for x in range(0, x):
        print("####")


def eyes(boolean):
    if boolean:
        print("----")
        print('@  @')

    elif not boolean:
        print('@  @')


def nose(nos):
    print(" " + (str(nos) * 2))


def mouth():
    print('====')


def main():
    hair(2)
    eyes(True)
    nose("`")
    mouth()


if __name__ == '__main__':
    main()
