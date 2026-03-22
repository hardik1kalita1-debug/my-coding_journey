from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def move(self):
        pass
class dog(animal):
    def move(self):
        print("dog runs")

class bird(animal):
    def move(self):
        print("bird flies")
class fish(animal):
    def move(self):
        print("fish swims")
d=dog()
b=bird()
f=fish()

d.move()
b.move()
f.move()
