import math

class Point:
    "Represents a point in two-dimensional geometric coordinates"

    def __init__(self, new_x=0, new_y=0):
        # note on keyword arguments: we can choose which one to specify
        # e.g. p = Point(new_y=3)

        # the chunk below is a "docstring"
        """Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the
        point defaults to the origin."""

        self.move(new_x, new_y)

    def reset(self):
        "Reset the point back to the geometric origin: 0, 0"

        self.move(0, 0)

    def move(self, new_x, new_y):
        "Move the point to a new location in 2D space."

        self._x = new_x
        self._y = new_y

    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second
        point passed as a parameter.

        This function uses the Pythagorean Theorem to calculate
        the distance between the two points. The distance is
        returned as a float."""
        
        return math.sqrt(
            (self._x - other_point._x)**2 +
            (self._y - other_point._y)**2
        )

    def print(self):
        "Prints the coordinates like (x, y)."

        print(f"({self._x}, {self._y})") 


# only run this if the file is run as "__main__"
# (run from command line)
if __name__ == "__main__":
    p1 = Point(5, 10)
    p2 = Point(4, 2)

    p1.move(5, 5)

    p1.print()
    p2.print()

    print(p1.calculate_distance(p2))

