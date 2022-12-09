
class Worker():

    WORKERS = ["A", "B", "Y", "Z"]

    def __init__(self, name, row, col):
        self._name = name
        self._row = row
        self._col = col

    def get_name(self):
        return self._name
    
    def get_row(self):
        return self._row

    def set_row(self, row):
        self._row = row

    def get_col(self):
        return self._col

    def set_col(self, col):
        self._col = col

    row = property(get_row, set_row)
    col = property(get_col, set_col)

    def move(self, row, col):
        """Move the worker to given row and col."""
        self._row = row
        self._col = col

    def occupyCell(self, row, col):
        """Check if the worker occupies the given cell."""
        if self.row == row and self.col == col:
            return True
        else:
            return False

    def getDistanceFrom(self, row, col):
        """Get distance of the worker from the given cell."""
        return max(abs(self._row - row), abs(self._col - col))

    def makeCopy(self):
        """"Make a copy of the current worker."""
        return Worker(self._name, self._row, self._col)