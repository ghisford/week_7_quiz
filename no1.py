#1. Your task is to create slightly different animals, which should have 
# the same properties and methods, but should implement the talk() method 
# in different ways. For example. should a cat (when talking) say "Moew", 
# a dog "Woff", a fish "Blub" and a Cow "Muuu". They should all share the
#  following (private) properties: name (string), age (number), food (list of strings), 
# and have the functions get_name, set_name, get_age, set_age, get_food, 
# add_food, remove_food. Finally, all the animals must have the talk function, 
# but that function must, as I said, be implemented in each animal, as the animals 
# have different sounds.
# When you have made the classes, create instances of the classes and put in a list 
# - loop through the list - and let all the animals talk! :)


import string


class Animal:

    __name = ''
    __age = 0
    __food = []

    def __init__(self,name:string,age:int,food:list):
        self.__name = name
        self.__age = age
        self.__food = food


    def talk(self):
        print("sound")


# name
    def get_name(self):
        return self.__name 

    def set_name(self,name):
        self.__name = name


# age
    def get_age(self):
        return self.__age 

    def set_age(self,age):
        self.__age = age


# food
    def get_food(self):
        return self.__food 

    def set_food(self,food):
        self.__food = food

    def remove_food(self):
        del self.__food 


# animals

class Cat(Animal):
    def talk(self):
        print("meow")

class Dog(Animal):
    def talk(self):
        print("woof")

class Fish(Animal):
    def talk(self):
        print("bub")

class Cow(Animal):
    def talk(self):
        print("muuu")


















































