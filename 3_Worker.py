class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return f'Сотрудник {self.name} {self.surname} имеет доход {total_income} р.'


b = Position('Alex', 'Alypin', 'Administrator', 10, 11)
print(b.get_full_name())
print(b.get_total_income())
print(b.name)
print(b.surname)
print(b.position)
