from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


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
        if self.size() == other.size():
            new_rows = []
            for index in range(self.size()[0]):
                new_rows.append(
                    list(map(lambda a: a[0] + a[1],
                             zip(self.rows[index], other.rows[index])))
                )
        else:
            raise MatrixError(self, other)

        return Matrix(new_rows)

    def __mul__(self, other):
        """
        Multiplication of matrix by number
        :param other: alpha number
        :return: new Matrix object
        """
        if isinstance(other, int) or isinstance(other, float):
            new_rows = []
            for index in range(self.size()[0]):
                new_rows.append(
                    list(map(lambda a: a[0] * a[1],
                             zip(self.rows[index], [other] * self.size()[1])))
                )

            return Matrix(new_rows)
        elif isinstance(other, Matrix):
            if self.size()[1] == other.size()[0]:
                s = 0  # sum of elements
                row_list = []    # row in matrix
                new_rows = []   # final new matrix
                # count of rows in 1st matrix
                for row1 in range(0, self.size()[0]):
                    # count of columns in 2nd matrix
                    for j in range(0, other.size()[1]):
                        # count of columns in 1st matrix
                        for i in range(0, self.size()[1]):
                            s = s + self.rows[row1][i] * other.rows[i][j]
                        row_list.append(s)
                        s = 0
                    new_rows.append(row_list)
                    row_list = []
                return Matrix(new_rows)
            else:
                raise MatrixError(self, other)

    __rmul__ = __mul__

    def transpose(self):
        """
        Transpose matrix, update exist object
        :return: transposed exist matrix object
        """
        self.rows = [list(l) for l in zip(*self.rows)]
        return self

    @staticmethod
    def transposed(matrix):
        """
        Transpose input matrix object
        :param matrix:
        :return: new transposed matrix object
        """
        matrix = Matrix(matrix.rows).transpose()
        return matrix

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
