# Class
class Fan:
    def __init__(self, make, radius, color):
        self.make = make
        self.radius = radius
        self.color = color
        self.speed = 0
        self.is_on = False

    def __repr__(self):
        return repr((self.make, self.radius, self.color, self.speed, self.is_on))

    def switch_on(self):
        self.is_on = True
        self.speed = 3

    def switch_off(self):
        self.is_on = False
        self.speed = 0

    def increase_speed(self):
        self.speed += 1
        if self.speed >5:
            self.speed = 5

    def decrease_speed(self):
        self.speed -= 1
        if self.speed == 0:
            self.is_on = False


fan = Fan('Manufacturer 1', 5, 'Green')
fan.switch_on()
print(fan)
fan.increase_speed()
print(fan)
fan.increase_speed()
print(fan)
fan.increase_speed()
print(fan)
fan.decrease_speed()
fan.decrease_speed()
fan.decrease_speed()
fan.decrease_speed()
print(fan)
fan.decrease_speed()
print(fan)


# State:
# make
# radius
# color
# speed
# is_on
#
# Behavior:
# switch_on
# switch_off
# increase_speed
# descrease_speed
