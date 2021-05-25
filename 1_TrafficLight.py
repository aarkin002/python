import time


class TrafficLight:
    __color = {}

    def running(self):
        __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 3}
        for color in __color:
            self.color = color
            print(self.color, '- ждите', __color[color], 'сек')
            time.sleep(__color[color])


t_light = TrafficLight()
t_light.running()
