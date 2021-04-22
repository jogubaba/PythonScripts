class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass


Blue = Dog()
Jax = Cat()
Blue.bark()
Blue.walk()
Jax.walk()

