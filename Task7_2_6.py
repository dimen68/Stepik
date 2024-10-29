# Классный прямоугольник 2.0
class Rectangle:
    def __init__(self, *args):
        self.x0 = round(args[0][0], 2)
        self.y0 = round(args[0][1], 2)
        self.x1 = round(args[1][0], 2)
        self.y1 = round(args[1][1], 2)
        self.x = round(abs(self.x0 - self.x1), 2)
        self.y = round(abs(self.y0 - self.y1), 2)

    def perimeter(self):
        return round(2 * (self.x + self.y), 2)

    def area(self):
        return round(self.x * self.y, 2)

    def get_pos(self):  # возвращает координаты верхнего левого угла в виде кортежа;
        self.high_left_corn = []
        if self.x0 < self.x1:
            self.high_left_corn.append(self.x0)
        else:
            self.high_left_corn.append(self.x1)
        if self.y0 > self.y1:
            self.high_left_corn.append(self.y0)
        else:
            self.high_left_corn.append(self.y1)
        return tuple(self.high_left_corn)

    def get_size(self):  # возвращает размеры в виде кортежа;
        return tuple([self.x, self.y])

    def move(self, dx, dy):  # изменяет положение на заданные значения;
        self.x0 = round(self.x0 + dx, 2)
        self.x1 = round(self.x1 + dx, 2)
        self.y0 = round(self.y0 + dy, 2)
        self.y1 = round(self.y1 + dy, 2)

    def resize(self, width, height):  # изменяет размер (положение верхнего левого угла остаётся неизменным).
        if self.x0 < self.x1:
            self.x1 = self.x0 + width
        else:
            self.x0 = self.x1 + width
        self.x = round(abs(self.x0 - self.x1), 2)
        if self.y0 > self.y1:
            self.y1 = self.y0 - height
        else:
            self.y0 = self.y1 - height
        self.y = round(abs(self.y0 - self.y1), 2)


if __name__ == '__main__':
    rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    print(rect.get_pos(), rect.get_size())
    rect.move(1.32, -5)
    print(rect.get_pos(), rect.get_size())

    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    print(rect.get_pos(), rect.get_size())
    rect.resize(23.5, 11.3)
    print(rect.get_pos(), rect.get_size())
