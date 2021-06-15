class Human():
    # Private var
    __privateVar = "this is __private variable"

    # Constructor method
    def __init__(self):
        self.className = "Human class constructor"
        self.__privateVar = "this is redefined __private variable"

    # Public method
    def showName(self, name):
        self.name = name
        return self.__privateVar + " " + name

    # Private method
    def __privateMethod(self):
        return "Private method"

    # Public method that returns a private variable
    def showPrivate(self):
        return self.__privateMethod()

    def showProtecded(self):
        return self._protectedMethod()


class Male(Human):
    def showClassName(self):
        return "Male"

    def showPrivate(self):
        return self.__privateMethod()

    def showProtected(self):
        return self._protectedMethod()


class Female(Human):
    #super().__init__("hi")
    def showClassName(self):
        return "Female"

    def showPrivate(self):
        return self.__privateMethod()


human = Human()
print(human.className)
print(human.showName("Vasya"))
print(human.showPrivate())

male = Male()
print(male.className)
print(male.showClassName())
print(male.showProtected())

female = Female()
print(female.className)
print(female.showClassName())
#print(female.showPrivate())

#female._Human__privateVar