class Car:
    def __init__(self):
        self.color="Red"
        self.Seats="4Seater"
        print(self.color)
        print(self.Seats)
        self.speed=50
        
    def Accelerate(self):
        self.speed=self.speed+10
        return self.speed
    def Break(self):
        self.speed=self.speed-10
        return self.speed

Benz=Car()
print(Benz.Accelerate())
