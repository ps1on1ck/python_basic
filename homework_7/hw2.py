# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм.У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_flow_rate(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v > 0:
            self.__v = v
        else:
            raise ValueError(f'This value of {v} must be greater than 0')

    def fabric_flow_rate(self):
        return f"Fabric consumption: {round(self.v / 6.5 + 0.5, 2)}"


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        self.__h = h

    def fabric_flow_rate(self):
        return f"Fabric consumption: {2 * self.h + 0.3}"


coat = Coat(2)
print(coat.fabric_flow_rate())
coat.v = 7
print(coat.fabric_flow_rate())

try:
    coat.v = -5
except ValueError as err:
    print(err)

print("------")

costume = Costume(2)
print(costume.fabric_flow_rate())
costume.h = 1.5
print(costume.fabric_flow_rate())
