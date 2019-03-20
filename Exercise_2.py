#2.1
class RectangularArea:
    """Class for work with square geometric instances """
    def __init__(self, side_a, side_b):
        """
        Defines to parameters of RectangularArea class. Checks parameters type.
        :param side_a: length of side a
        :param side_b:length of side a
        """
        self.side_a = side_a
        self.side_b = side_b
        if type(self.side_a) and type(self.side_b) == int or float:
            pass
        else:
            raise Exception("Wrong type, sides should be int or float")

    def square(self):
        """
        :return: value of square for class instance
        """
        return self.side_a * self.side_b

    def perimeter(self):
        """
        :return: alue of square for class instance
        """
        return (self.side_b + self.side_a)*2


#2.2
class Dot:
    """Defines coordinates of the dot on the map"""
    def __init__(self, x, y):
        """
        :param x: distance from point x to y-axis
        :param y: distance from point y to x-axis
        """
        self.x = x
        self.y = y

    def dist_from_zero_version1(self):
        """
        :return: the distance on the plain from the dot to the origin
        """
        x1 = 0
        y1 = 0
        d = ((self.x-x1)**2 + (self.y - y1)**2)**0.5
        return d

    def dist_from_zero_version2(self, x2=0, y2=0):
        """
        :param x2: origin of x-axis (by default)
        :param y2: origin of y-axis (by default)
        :return: :return: the distance on the plain from the dot to the origin
        """
        dv2 = ((self.x-x2)**2 + (self.y - y2)**2)**0.5
        return dv2

    def between_two_dots(self, x3, y3): # I am not sure that this is correct way to solve your exercise
        """
        :param x3: distance from point x to y-axis
        :param y3: distance from point y to x-axis
        :return: the distance on the plain between two dots
        """
        d = ((self.x - x3) ** 2 + (self.y - y3) ** 2) ** 0.5
        return d
    def three_dimensional(self, z): # Maybe I misunderstood the task. My method looks weird
        """
        Converts coordinates to three_dimensional system
        :param z: distance from point x to xy plane
        :return: coordinates of the dot in three_dimensional system
        """
        return (self.x, self.y, z)


if __name__ == "__main__":
    rect = RectangularArea(10, 12)
    print(rect.square())
    print(rect.perimeter())
    dot1 = Dot(20,20)
    print(dot1.dist_from_zero_version1())
    print(dot1.dist_from_zero_version2())
    print(dot1.between_two_dots(34.4, 45))
    print(dot1.three_dimensional(12))


