from pytms.utils.point import Point

class Rectangle:
    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.left = self.x
        self.right = self.x + width
        self.top = self.y
        self.bottom = self.y + height

    def __str__(self):
        return f'X:{self.x} Y:{self.y} Width:{self.width} Height:{self.height}'

    def get_location(self):
        return Point(self.x, self.y)

    def set_location(self, point):
        self.x = point.x
        self.y = point.y

    def get_center(self):
        return Point(self.x + self.width / 2, self.y + self.height / 2)

    def is_empty(self):
        if self.width == 0 and self.height == 0 and self.x == 0:
            return self.y == 0
        return False

    def offset(self, amount: Point):
        self.x += amount.x
        self.y += amount.y

    def inflate(self, horizontal_amount, vertical_amount):
        self.x -= int(horizontal_amount)
        self.y -= int(vertical_amount)
        self.width += int(horizontal_amount) * 2
        self.height += int(vertical_amount) * 2

    def contains_point(self, value: Point):
        if self.x <= value.x < self.x + self.width and self.y <= value.y:
            return value.y < self.y + self.height
        return False

    def contains_rectangle(self, value):
        if self.x <= value.x and value.x + value.width <= self.x + self.width and self.y <= value.y:
            return value.y + value.height <= self.y + self.height
        return  False


    def intersects(self, value):
        if value.x < self.x + self.width and self.x < value.x + value.width and value.y < self.y + self.height:
            return self.y < value.y + value.height
        return False

    @staticmethod
    def intersect(value1, value2):
        num = value1.x + value1.width
        num2 = value2.x + value2.width
        num3 = value1.y + value1.height
        num4 = value2.y + value2.height
        num5 = value1.x if value1.x > value2.x else value2.x
        num6 = value1.y if value1.y > value2.y else value2.y
        num7 = num if num < num2 else num2
        num8 = num3 if num3 < num4 else num4

        result = Rectangle()

        if num7 > num5 and num8 > num6:
            result.x = num5
            result.y = num6
            result.width = num7 - num5
            result.height = num8 - num6
        else:
            result.x = 0
            result.y = 0
            result.width = 0
            result.height = 0

        return result

    @staticmethod
    def union(value1, value2):
        num = value1.x + value1.width
        num2 = value2.x + value2.width
        num3 = value1.y + value1.height
        num4 = value2.y + value2.height
        num5 = value1.x if value1.x < value2.x else value2.x
        num6 = value1.y if value1.y < value2.y else value2.y
        num7 = num if num > num2 else num2
        num8 = num3 if num3 > num4 else num4
        result = Rectangle(num5, num6, num7-num5, num8-num6)
        return result

    def equals(self, other):
        """
        Checks if given object is a Rectangle and if so, checks if its equal to this one
        :param other:
        :return:
        """
        if not isinstance(other, Rectangle):
            return False
        if self.x == other.x and self.y == other.y and self.width == other.width:
            return self.height == other.height

        return False