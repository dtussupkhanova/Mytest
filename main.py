#Первая задача
'''
from time import sleep

class TrafficLight:
    __colors = ['Red','Yellow','Green']

    def running(self):
        mode = 0
        while True:
            if mode == 0:
                print('Красный. Остановитесь')
                sleep(7)
                mode += 1
            elif mode == 1:
                print('Желтый. Приготовьтесь')
                sleep(2)
                mode += 1
            elif mode == 2:
                print('Зеленый. Едьте')
                sleep(5)
                mode = 0

tl = TrafficLight()
tl.running()
'''
#Вторая задача
'''
class Road:
    def __init__(self, length, width):
        self._l = length
        self._w = width
        print(f'Length: {self._l}, Width: {self._w}')

    def mass(self):
        return round(self._l*self._w*25*5/1000)

r = Road(20, 5000)
print(r.mass())
'''
#Третья задача
'''
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.n = name
        self.s = surname
        self.p = position
        self._i = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.n + ' ' + self.s

    def get_total_income(self):
        return f'{sum(self._i.values())}'

w1 = Position('Alex', 'Voronov', 'Manager', 50000, 10000)
print(w1.get_full_name())
print(w1.p)
print(w1.get_total_income())
'''
#Четвертая задача
'''
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed>60:
            print('Вы превысили скорость')

class WorkCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print('Вы превысили скорость')


car = Car(50,'green','Daewoo',True)
car.go()
car.stop()
car.turn('налево')
tc = TownCar(80,'black','Toyota',False)
tc.show_speed()
'''
#Пятая задача
'''
class Stationery:
    def __init__(self, title):
        self.t = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Запуск отрисовки маркером')

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
'''

