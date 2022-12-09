class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length, *args, **kwargs):
        # don't technically need *args and **kwargs now,
        # but useful if, say, in the future, Rectangle also takes a color
        super().__init__(length, length, *args, **kwargs)

class Triangle(Rectangle):
    def area(self):
        return super().area() / 2

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length