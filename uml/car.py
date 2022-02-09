from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def get_brand(self):
        pass


class Mercedes(Car):
    def get_brand(self):
        return "Mercedes"


class Toyota(Car):
    def get_brand(self):
        return "Toyota"


class Volvo(Car):
    def __init__(self):
        self.extra_safe = True

    def get_brand(self):
        return "Volvo"


class Kia(Car):
    def get_brand(self):
        return 'Kia'


class Bmw(Car):
    def get_brand(self):
        return 'Bmw'


class Porsche(Car):
    def get_brand(self):
        return 'Porsche'


if __name__ == '__main__':
    cars = [
        Mercedes(),
        Volvo(),
        Toyota(),
        Kia(),
        Bmw(),
        Porsche(),
    ]

    for car in cars:
        print(car.get_brand())
