import math


class Vector2:
    # static methods
    @staticmethod
    def _zero():
        return Vector2(0, 0)

    @staticmethod
    def _one():
        return Vector2(1, 1)

    @staticmethod
    def _unit_x():
        return Vector2(1, 0)

    @staticmethod
    def _unit_y():
        return Vector2(0, 1)

    @staticmethod
    def distance(value1, value2):
        """
        Given 2 vectors, returns the distance between them
        :param value1:
        :param value2:
        :return:
        """
        num = float(value1.x - value2.x)
        num2 = float(value1.y - value2.y)
        num3 = float(num ** 2 + num2 ** 2)
        return float(math.sqrt(num3))

    @staticmethod
    def distance_squared(value1, value2):
        """
        Given 2 vectors, returns the squared distance between them
        :param value1:
        :param value2:
        :return:
        """
        num = float(value1.x - value2.x)
        num2 = float(value1.y - value2.y)
        return num ** 2 + num2 ** 2

    @staticmethod
    def dot(value1, value2):
        """
        Given 2 vectors, returns their dot product
        :param value1:
        :param value2:
        :return:
        """
        return value1.x * value2.x + value1.y * value2.y

    @staticmethod
    def reflect(vector, normal):
        num = float(vector.x * normal.x + vector.y * normal.y)
        result = Vector2()

        result.x = vector.x - float(2) * num * normal.x
        result.y = vector.y - float(2) * num * normal.y

        return result

    @staticmethod
    def min(value1, value2):
        """
        Returns the min x and y from 2 vectors as a new Vector2
        :param value1:
        :param value2:
        :return:
        """
        result = Vector2()

        if value1.x < value2.x:
            result.x = value1.x
        else:
            result.x = value2.x

        if value1.y < value2.y:
            result.y = value1.y
        else:
            result.y = value2.y

        return result

    @staticmethod
    def max(value1, value2):
        """
        Returns the max x and y from 2 vectors as a new Vector2
        :param value1:
        :param value2:
        :return:
        """
        result = Vector2()

        if value1.x > value2.x:
            result.x = value1.x
        else:
            result.x = value2.x

        if value1.y > value2.y:
            result.y = value1.y
        else:
            result.y = value2.y

        return result

    @staticmethod
    def clamp(vector, min_vec, max_vec):
        """
        Clamps a vector between 2 minimum and maximum vectors
        :param vector:
        :param min_vec:
        :param max_vec:
        :return:
        """
        x = vector.x
        x = max_vec.x if x > max_vec.x else x
        x = min_vec.x if x < min_vec.x else x

        y = vector.y
        y = max_vec.y if y > max_vec.y else y
        y = min_vec.y if y < min_vec.y else y

        result = Vector2(x, y)

        return result

    @staticmethod
    def lerp(value1, value2, amount):
        amount = float(amount)

        result = Vector2()
        result.x = value1.x + (value2.x - value1.x) * amount
        result.y = value1.y + (value2.y - value1.y) * amount

        return result

    @staticmethod
    def barycentric(value1, value2, value3, amount1, amount2):
        amount1, amount2 = float(amount1), float(amount2)
        result = Vector2()
        result.x = value1.x + amount1 * (value2.x - value1.x) + amount2 * (value3.x - value1.x)
        result.y = value1.y + amount1 * (value2.y - value2.y) + amount2 * (value3.y - value1.y)

        return result

    @staticmethod
    def smooth_step(value1, value2, amount):
        amount = float(amount)
        amount = float(1) if amount > float(1) else (float(0) if amount < float(0) else amount)
        amount = amount * amount * (float(3) - float(2) * amount)
        result = Vector2()
        result.x = value1.x + (value2.x - value1.x) * amount
        result.y = value1.y + (value2.y - value1.y) * amount

        return result

    # static fields
    zero = lambda z: Vector2._zero()
    one = lambda o: Vector2._one()
    unit_x = lambda ux: Vector2._unit_x()
    unit_y = lambda uy: Vector2._unit_y()

    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f'X:{self.x} Y:{self.y}'

    def equals(self, obj):
        """
        Checks if a given object is a Vector2 and if so, checks if its equal to this Vector2
        :param obj:
        :return:
        """
        if isinstance(obj, Vector2):
            if obj.x == self.x and obj.y == self.y:
                return True
        return False

    def __len__(self):
        return self.get_length()

    def get_length(self):
        """
        Returns the length of the vector
        :return:
        """
        num = float(self.x ** 2 + self.y ** 2)
        return float(math.sqrt(num))

    def get_length_squared(self):
        """
        Returns the squared length of the vector
        :return:
        """
        return self.x ** 2 + self.y ** 2

    def normalize(self):
        """
        Normalizes the vector
        :return:
        """
        num = float(self.x ** 2 + self.y ** 2)
        num2 = float(1) / float(math.sqrt(num))
        self.x *= num2
        self.y *= num2
