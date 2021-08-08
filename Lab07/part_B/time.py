class Time:
    def __init__(self, time):
        self.time = time

    def __str__(self):

        return f"{(self.formatted())} "

    def formatted(self):
        hours = self.time // 60
        minutes = self.time % 60
        tf = f"{hours} h {minutes} min"
        return tf


def main():
    t1 = Time(int(input('Enter number of minutes (positive integer) -> ')))
    print(t1)


if __name__ == '__main__':
    main()
