# 9. Using only functions and lists, Implement a queue data structure. 
# The queue should have the following methods: enqueue, dequeue, and size. 
# The queue should be "first-in-first-out" (FIFO).
list_1 = list()
maximum = 5

def isEmpty():
    return len(list_1) == 0    

def isFull():
    return len(list_1) == maximum



def enqueue(element):
    if not isFull():
        list_1.insert(0,element)
        return list_1
    else:
        return 'list is already full'


def dequeue():
    if not isEmpty():
        list_1.pop()
        return list_1

    else:
        return 'yo the list is already empty'

def size(f):
    print(len(list_1))
