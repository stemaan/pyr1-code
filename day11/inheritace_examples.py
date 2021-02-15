class Vehicle:
    def __init__(self, name):
        self.name = name
        self.wheels_quantity = 1
        print('Initializing', self.name)

    def drive(self):
        print('Driving')

    def stop(self):
        print('Stopped')


class Unicycle(Vehicle):
    def balance(self):
        print('Trying not to fall down')


class Bicycle(Vehicle):
    def __init__(self, name):
        super().__init__(name)  # Vehicle.__init__(self, name)
        self.wheels_quantity = 2

    def ring(self):
        print('Ringing!')

    def drive(self):
        super().drive()  # Vehicle.drive(self)
        print('All i want is bicycle!')


class MountainBicycle(Bicycle):
    def drive(self):
        print('Sometimes hiking always biking')


if __name__ == '__main__':
    something = Vehicle('Unknown')
    canondale = Bicycle('Canondale')
    unicycle = Unicycle('Unicykl')
    mtb = MountainBicycle('Specialized')
    print(mtb.name)
    print(mtb.wheels_quantity)
    mtb.drive()
    mtb.stop()
    mtb.ring()

    something.drive()
    something.stop()

    unicycle.drive()
    unicycle.stop()
    unicycle.balance()
    print(unicycle.wheels_quantity)
    print(unicycle.name)

    canondale.ring()
    canondale.drive()
    canondale.stop()
