
class Car:

    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self):
        print(" I'am in Car run ")

    def stop(self):
        print(" I'am in Car stop ")
