class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationery):
    pass

class Pencil(Stationery):
    pass

class Handle(Stationery):
    pass

pen = Pen('Ручка')
print(pen.draw())
pencil = Pencil('Карандаш')
print(pencil.draw())
handle = Handle("Маркер")
print(handle.draw())
print(pen.draw())