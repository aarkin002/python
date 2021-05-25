class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asphalt_weight(self, bag_weight, a_height):
        a_weight = self._length * self._width * bag_weight * a_height / 1000
        print('Масса асфальта = ', a_weight, 'т.')


road_weight = Road(20, 5000)
road_weight.asphalt_weight(25, 5)
