import math


class Cell:
    def __init__(self, count_cell):
        self.count_cell = count_cell

    def __add__(self, other):
        return f'Cложение : {Cell(self.count_cell + other.count_cell)}'

    def __sub__(self, other):
        return f'Разность : {Cell(self.count_cell - other.count_cell)}'

    def __mul__(self, other):
        return f'Умножение : {Cell(self.count_cell * other.count_cell)}'

    def __truediv__(self, other):
        return f'Деление с округлением до целого : {Cell(self.count_cell / other.count_cell)}'

    def __str__(self):
        sub_cell = float(f'{self.count_cell}')
        if sub_cell > 0:
            return f'{math.ceil(self.count_cell)}'
        else:
            return f'Отрицательный результат'

    def make_order(self, row_cell):
        self.row_cell = row_cell
        a = self.count_cell // row_cell
        b = f'{row_cell * "*"}\\n'
        c = f'{self.count_cell % row_cell * "*"}'
        return f'{a * b}{c}'


cell_1 = Cell(5)
cell_2 = Cell(33)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print("\nЧудо строка с рядами и ячейками:\n", cell_2.make_order(5))
