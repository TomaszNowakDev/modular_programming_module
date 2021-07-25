def sing_verse(bottles):
    print(f'{bottles} green bottles hanging on the wall,')
    print(f'{bottles} green bottles hanging on the wall,')
    print('And if one green bottle should accidentally fall,')
    print(f"There'll be {bottles - 1} green bottles hanging on the wall.")
    print()


def second_last_verse():
    print(f'Two green bottles hanging on the wall,')
    print(f'Two green bottles hanging on the wall,')
    print('And if one green bottle should accidentally fall,')
    print(f"There'll be 1 green bottle hanging on the wall.")


def last_verse():
    print(f'One green bottle hanging on the wall,')
    print(f'One green bottle hanging on the wall,')
    print('And if one green bottle should accidentally fall,')
    print("There'll be no green bottles hanging on the wall.")


def main():
    for x in range(20, 2, -1):
        sing_verse(x)
    second_last_verse()
    print()
    last_verse()


if __name__ == '__main__':
    main()
