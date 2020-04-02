class Animal:
        def __init__(self):
            pass

        def __repr__(self):
            pass

        def bark(self):
            print('bark')


animal = Animal()
animal.bark()


class Pet(Animal):
    def groom(self):
        print("groom")

pet = Pet()
pet.bark()
pet.groom()




