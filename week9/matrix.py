from sys import stdin


class Matrix:
    def __init__(self, lists):
        self.rows = [row.copy() for row in lists]

    def size(self):
        """
        Method which returns number of rows and columns
        :return: (num_rows, num_cols)
        """
        return len(self.rows), len(self.rows[0])

    def __add__(self, other):
        """
        Add 2 equivalent size matrices
        :param other: second Matrix
        :return: new Matrix object
        """
        new_rows = []
        for index in range(self.size()[0]):
            new_rows.append(
                list(map(lambda a: a[0] + a[1],
                         zip(self.rows[index], other.rows[index])))
            )
        return Matrix(new_rows)

    def __mul__(self, other):
        """
        Multiplication of matrix by number
        :param other: alpha number
        :return: new Matrix object
        """
        new_rows = []
        for index in range(self.size()[0]):
            new_rows.append(
                list(map(lambda a: a[0] * a[1],
                         zip(self.rows[index], [other] * self.size()[1])))
            )
        return Matrix(new_rows)

    __rmul__ = __mul__

    def __str__(self):
        """
        Transform object representation to string
        :return: str
        """
        represent = ''
        for i, row in enumerate(self.rows, start=1):
            represent += '\t'.join(map(str, row))
            if i < len(self.rows):
                represent += '\n'
        return represent


exec(stdin.read())
