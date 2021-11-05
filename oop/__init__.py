class Car:
    def __init__(self, name):
        self._name=name

    def GetOwner(self):
        try:
            print('owner is ', self._name)
        except Exception:
            print("there is now owner for this instance")



def main():
    mycar = Car("meguenni")
    mycar.GetOwner()


if __name__ == '__main__':
    main()
