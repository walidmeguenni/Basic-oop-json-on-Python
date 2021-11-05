# library for for time
import datetime


def main():
    uryears = input('Enter your year : ')  # methode to entre value from console
    cuyears = datetime.datetime.now().year
    age = cuyears - int(uryears)
    print("your age is {} years.".format(age))


if __name__ == '__main__':
    main()
