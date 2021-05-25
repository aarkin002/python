from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, clothes):
        self.clothes = clothes

    @abstractmethod
    def cost_cloth(self):
        pass


class Coat(Clothes):
    @property
    def cost_cloth(self):
        cost = self.clothes / 6.5 + 0.5
        return f'На пальто будет потрачено: {cost} ткани'


class Suit(Clothes):
    @property
    def cost_cloth(self):
        cost = self.clothes * 2 + 0.3
        return f'На костюм будет потрачено: {cost} ткани'


coat = Coat(5)
print(coat.cost_cloth)
suit = Suit(5)
print(suit.cost_cloth)
