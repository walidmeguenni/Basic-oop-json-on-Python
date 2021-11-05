class Person:
    def __init__(self, name, lastname):
        self._name = name
        self._lastName = lastname

    def setName(self, name):
        self._name = name

    def setLastName(self, lastname):
        self._lastName = lastname

    def getName(self):
        print('Name', self._name)

    def getLastName(self):
        print('LastName', self._lastName)


class Student(Person):  # extends
    def __init__(self, name, lastname, school):
        self._school = school
        Person.__init__(self, name, lastname)

    def setSchool(self, school):
        self._school = school

    def getSchool(self):
        print('shcool of {} is {}'.format(self._name, self._school))
        

def main():
    student = Student("walid", "meguenni", "kkkk")
    student.setSchool("home")
    student.getSchool()


if __name__ == '__main__':
    main()
