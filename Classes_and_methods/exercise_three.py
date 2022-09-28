# můžu volat také nekonečno metod
class Plane:
    def __init__(self) -> None:
        self.drive()
        self.flaps()
        self.speed()
        self.wheels()
        self.alarm()

    def drive(self):
        print('accelerating')

    def flaps(self):
        print('closing flaps')

    def speed(self):
        print('uppering speed')

    def wheels(self):
        print('retracting the wheels')

    def alarm(self):
        print('We all gonna DIE!')
    
Mig21 = Plane()