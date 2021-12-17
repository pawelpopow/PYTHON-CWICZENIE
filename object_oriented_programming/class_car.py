class Car:

    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def drive(self):
        print('Bru bru')

class Mercedes(Car):

    def __init__(self, speed, color):
        super.__init__(self, speed, color)



if __name__ == '__main__':
    car = Car(speed=120, color='green')

