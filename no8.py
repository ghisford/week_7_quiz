# 8.Using list comprehension, write a program that 
# takes a list of numbers and returns a list of the squares of the numbers.
def sq(list_1):
    list_2 = [i**2 for i in list_1]
    return list_2

print(sq([10]))