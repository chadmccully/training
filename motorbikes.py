# #Motorbike
class Motorbike:
    def __init__(self, speed):
        self.speed = speed

    def increase_speed(self, how_much):
        self.speed += how_much

    def decrease_speed(self, how_much):
        self.speed -= how_much


honda = Motorbike(50)
ducati = Motorbike(250)


print(honda.speed)
print(ducati.speed)

honda.increase_speed(75)
ducati.increase_speed(25)

print(honda.speed)
print(ducati.speed)

honda.decrease_speed(5)
print(honda.speed)