class LandAnimal:
    def __init__(self):
        super().__init__()
        self.walking_speed = 5

    def increase_walking_speed(self, rate_change):
        self.walking_speed += rate_change

class WaterAnimal:
    def __init__(self):
        super().__init__()
        self.swimming_speed = 10

    def increase_swimming_speed(self, rate_change):
        self.swimming_speed += rate_change


class Amphibian(WaterAnimal, LandAnimal):
    def __init__(self):
        super().__init__()

amphibian = Amphibian()
print(amphibian.swimming_speed, amphibian.walking_speed)

amphibian.increase_walking_speed(10)

print(amphibian.swimming_speed, amphibian.walking_speed)

amphibian.increase_swimming_speed(10)

print(amphibian.swimming_speed, amphibian.walking_speed)