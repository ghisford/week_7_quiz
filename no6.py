#6. Write a Python program that lists out all the default 
# as well as custom properties of the class.

class Boy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

nzima = Boy("ghislain", 24)

print(dir(nzima))