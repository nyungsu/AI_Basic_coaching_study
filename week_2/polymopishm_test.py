class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def talk(self):
        raise NotImplemented("subclass must implement")


class Cat(Animal):
    def talk(self):
        return "meow!"


class Dog(Animal):
    def talk(self):
        return "woof woof !"


animals = [Cat(name="missy"), Cat("abc"), Dog("dsfe")]

for animal in animals:
    print(animal.name + ":", animal.talk())
