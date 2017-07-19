class MyClass:
    def __init__(self):
        self.__name = "My Python Class"

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


#print MyClass().__name
mc = MyClass()

print mc._MyClass__name

print MyClass().get_name()

mc = MyClass()
mc.set_name("My New Cool Name")
print mc.get_name()