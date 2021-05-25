import numpy


class Matrix:
    def __init__(self, matrix_usr):
        self.matrix_usr = numpy.array(matrix_usr)

    def __str__(self):
        return f'{self.matrix_usr}'

    def __add__(self, other):
        return Matrix(self.matrix_usr + other.matrix_usr)


x = Matrix([[10, 20, 30], [40, 50, 60]])
print(x)
x1 = Matrix([[11, 23, 34], [43, 51, 62]])
print(x + x1)
