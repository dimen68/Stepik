# Классная точка 2.0
class Point:
    def __init__(self, first, second):
        self.x = first
        self.y = second

    def move(self, new_first, new_second):
        self.x += new_first
        self.y += new_second

    def length(self, other):
        return round((((self.x - other.x)**2 + (self.y - other.y)**2)**0.5),2)


point = Point(3, 5)
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)

first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))