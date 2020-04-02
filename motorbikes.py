# Class
class Motorbike:
    def __init__(self, speed):
        self.speed = speed

    # Behavior
    def increase_speed(self, how_much):
        self.speed += how_much

    # Behavior
    def decrease_speed(self, how_much):
        if(self.speed-how_much>0):
            self.speed -= how_much
        else:
            print("Get a life")

# Instance 1 or object 1
honda = Motorbike(50)

# Instance 2 or object 2
ducati = Motorbike(250)


print(honda.speed)
print(ducati.speed)

honda.increase_speed(75)
ducati.increase_speed(25)

print(honda.speed)
print(ducati.speed)

honda.decrease_speed(5)
print(honda.speed)

honda.decrease_speed(300)