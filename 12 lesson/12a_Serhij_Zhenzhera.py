'''
Task 1. Method overloading

Create a base class named Animal with a method called talk and then create two subclasses:
Dog and Cat, and make their own implementation of the method talk be different.
For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter   
'''


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError('Everyone speaks differently!')

    # на видео к уроку этот же генератор, но внешний, без функции
    def animals_talk(animals: list):
        for animal in animals:
            animal.talk()


class Dog(Animal):
    def talk(self):
        print(self.name, 'told: woof woof')


class Cat(Animal):
    def talk(self):
        print(self.name, 'told: meeeeeeeow')


if __name__ == "__main__":
    Animal.animals_talk([Cat('Lucky'), Dog('Sharik')])
    Animal.animals_talk([Cat('Pussy')])

'''
---output---
Lucky told: meeeeeeeow
Sharik told: woof woof
Pussy told: meeeeeeeow
'''
