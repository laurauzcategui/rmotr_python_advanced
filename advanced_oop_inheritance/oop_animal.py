#!/usr/bin/python


class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError()


# class Cat...
class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self,name)

    def talk(self):
        return "meow"
# class Dog...
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self,name)

    def talk(self):
        return "woof"


garfield = Cat(name='Garfield')
odie = Dog(name='Odie')

assert garfield.name == 'Garfield'
assert odie.name == 'Odie'

odie = Dog(name='Odie')
assert odie.talk() == 'woof'
