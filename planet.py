class Planet:
    def __init__(self, name="Earth"):
        self.speed = 10
        self.name = name
        self.distance_from_sun = 10000

    def rotate(self):
        print("rotate")

    def revolve(self):
        print("revolve")

    def rotate_and_revolve(self):
        print("rotate and revolve")
        self.rotate()
        self.revolve()

earth = Planet()
earth.rotate_and_revolve()







earth = Planet()
#earth.rotate_and_revolve()