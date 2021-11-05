class Car:
    def __init__(self, **kwargs):
        self._Data = kwargs

    def GetOwner(self):
        print("info is : ", self.Data)
        print("name", self.Data['Name'])
        print('address', self.Data['address'])

    def SetOwner(self, name):
        self.Data['Name'] = name


def main():
    mycar = Car(Name="meguenni",address="udsuds4")
    mycar.SetOwner("hakim")
    mycar.GetOwner()


if __name__ == '__main__':
    main()
