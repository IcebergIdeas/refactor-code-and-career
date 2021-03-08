class Rectangle(object):
    width = ""
    height = ""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # def get_area(self):
    #     return self.width * self.height

class ShapeProgram(object):

    rect1 = Rectangle(15, 30)
    area = rect1.width * rect1.height

    # better solution is to put area calculation of a rectangle into Rectangle object
    # area = rect1.get_area()
