from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    # abstract
    def bark(self):pass

class Dog(AbstractAnimal):
    def bark(self):
        print('Bow Wow')


print(Dog())
print(Dog().bark())
#print(AbstractAnimal())
