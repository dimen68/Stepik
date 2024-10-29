# Классный прямоугольник
class Rectangle:
    def __init__(self, *args):
        self.x0 = args[0][0]
        self.y0 = args[0][1]
        self.x1 = args[1][0]
        self.y1 = args[1][1]
        self.x = abs(self.x0 - self.x1)
        self.y = abs(self.y0 - self.y1)

    def perimeter(self):
        return round(2 * (self.x + self.y), 2)

    def area(self):
        return round(self.x * self.y, 2)


if __name__ == '__main__':
    rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    print(rect.perimeter())
    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    print(rect.area())
