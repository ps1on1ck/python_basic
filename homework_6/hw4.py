# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f"speed: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Нарушение скоростного режима")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Нарушение скоростного режима")


class PoliceCar(Car):
    pass


audi = PoliceCar(60, 'black', 'Audi', True)
print(f"speed: {audi.speed}")
print(f"name: {audi.name}")
print(f"is police: {audi.is_police}")
audi.go()
audi.turn('направо')
audi.show_speed()
audi.stop()

print("----------------")

volvo = WorkCar(80, 'black', 'Volvo')
print(f"speed: {volvo.speed}")
print(f"name: {volvo.name}")
print(f"is police: {volvo.is_police}")
volvo.go()
volvo.turn('влево')
volvo.show_speed()
volvo.stop()


print("----------------")


bmw = SportCar(160, 'black', 'BMW')
print(f"speed: {bmw.speed}")
print(f"name: {bmw.name}")
print(f"is police: {bmw.is_police}")
bmw.go()
bmw.turn('направо')
bmw.show_speed()
bmw.stop()

print("----------------")

mazda = TownCar(120, 'White', 'Mazda')
print(f"speed: {mazda.speed}")
print(f"name: {mazda.name}")
print(f"is police: {mazda.is_police}")
mazda.go()
mazda.turn('влево')
mazda.show_speed()
mazda.stop()
