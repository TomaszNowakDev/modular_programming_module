class Money:
    def __init__(self, sign, value):
        self.sign = sign
        self.value = value

    def __str__(self):
        return f"1 {self.sign} is {self.value}euro."

    def double(self):
        return self.value * 2

    def half(self):
        return self.value * .5


def main():
    m1 = Money("NEWCrypto", 1000)
    print(m1)
    print(f'NEWcrypto gained 100%, the current value {m1.double()}.')
    print(f'NEWcrypto lost 50%, the current value {m1.half()}.')


if __name__ == '__main__':
    main()
