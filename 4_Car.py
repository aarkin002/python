class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Car go'

    def stop(self):
        return f'Car stop'

    def turn(self, direction):
        self.direction = direction
        return f'Car turn {direction}'

    def show_speed(self):
        if self.speed > 0:
            return self.speed
        elif self.speed == 0:
            return f'Стоим'
        else:
            return f'Едем со скоростью {self.speed} (похоже назад)'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Вы превысили скорость'
        elif self.speed == 0:
            return f'Стоим'
        elif 0 < self.speed <= 60:
            return self.speed
        else:
            return f'Едем со скоростью {self.speed} (похоже назад)'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили скорость'
        elif self.speed == 0:
            return f'Стоим'
        elif 0 < self.speed <= 40:
            return self.speed
        else:
            return f'Едем со скоростью {self.speed} (похоже назад)'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(61, 'red', 'renault', True)
print(town_car.__dict__)
print(town_car.go())
print(town_car.stop())
print(town_car.turn('left'))
print(town_car.show_speed())

sport_car = SportCar(101, 'white', 'ferrari', False)
print(sport_car.__dict__)
print(sport_car.turn('right'))
print(sport_car.show_speed())

work_car = WorkCar(-49, 'green', 'cat', False)
print(work_car.__dict__)
print(work_car.turn('left'))
print(work_car.show_speed())

police_car = PoliceCar(0, 'black-white', 'lada', True)
print(police_car.turn('finish'))
print(police_car.show_speed())
print(police_car.__dict__)
