class Circle():
    def __init__(self, radius):
        """ Initialize self with radius """
        self.radius = radius
        

    def get_radius(self):
        """ Return self radius """
        return self.radius

    def set_radius(self, radius):
        """
        radius is a number
        Change self radius to radius
        """
        self.radius = radius

    def get_area(self):
        """ Return self area using pi = 3.14 """
        area = 3.14 * self.radius ** 2
        return area

    def equal(self, c):
        """
        c is a Circle object
        Return True if self and c have the same radius
        """
        if self.radius == c.radius:
            return True
        else:
            return False

    def bigger(self, c):
        """
        c is a Circle object
        Return self or c, the Circle object with the largest radius
        """
        if self.radius >= c.radius:
            return self
        else:
            return c