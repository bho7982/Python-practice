class MyClass:
    def __init__(self):
        self._name = "My Python Class"

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

print MyClass().get_name()

mc = MyClass()
mc.set_name("My New Cool Name")

print mc.get_name()