class NotFoundException(Exception):
    pass

class FoundException(Exception):
    pass


class GridFinder():
    def __init__(self, number, grid):

        # Defensive programming checked only once.
        assert isinstance(number, int)
        assert isinstance(grid, list)

        self.number = number
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        self.lower_bound_row = 0
        self.upper_bound_col = self.cols

        self.found_row = -1
        self.found_col = -1

    def __update_lower_bound_row(self):
        new_lower_bound_row = -1

        for i in range(self.lower_bound_row, self.rows):
            value = self.grid[i][self.upper_bound_col - 1]

            if value < self.number:
                new_lower_bound_row = i
                continue

            if self.number < value:
                break

            self.found_row = i
            self.found_col = self.upper_bound_col - 1
            raise FoundException()

        if new_lower_bound_row == self.rows - 1:
            raise NotFoundException()

        self.lower_bound_row = new_lower_bound_row

    def __update_upper_bound_col(self):

        new_upper_bound_col = self.upper_bound_col

        for column in range(self.upper_bound_col - 1, -1, -1):
            value = self.grid[self.lower_bound_row + 1][column]

            if self.number < value:
                new_upper_bound_col = column
                continue

            if value < self.number:
                break

            self.found_row = self.lower_bound_row + 1
            self.found_col = column
            raise FoundException()

        if new_upper_bound_col == 0:
            raise NotFoundException()

        self.upper_bound_col = new_upper_bound_col

    def search(self):
        """
        >>> f = GridFinder(2, [[1, 2], [3, 4]]); f.search()
        (0, 1)
        >>> f = GridFinder(3, [[1, 2], [3, 4]]); f.search()
        (1, 0)
        >>> f = GridFinder(0, [[1, 2], [3, 4]]); f.search() is None
        True
        >>> f = GridFinder(5, [[1, 2], [3, 4]]); f.search() is None
        True
        >>> f = GridFinder("abc", [[1, 2], [3, 4]])
        Traceback (most recent call last):
        ...
        AssertionError...
        >>> f = GridFinder(1, 123)
        Traceback (most recent call last):
        ...
        AssertionError...
        """

        if self.number < self.grid[0][0]:
            return None

        if self.grid[self.rows - 1][self.cols - 1] < self.number:
            return None

        try:
            while True:
                self.__update_lower_bound_row()
                self.__update_upper_bound_col()

        except NotFoundException:
            return None

        except FoundException:
            return self.found_row, self.found_col
