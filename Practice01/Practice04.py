class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height


print Rectangle(3, 4).get_area()

print Rectangle().get_area()