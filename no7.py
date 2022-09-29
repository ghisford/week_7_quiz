# 7. Write a Program in Python to implement a Stack
#  Data Structure using Class and Objects, with push, 
# pop, and traversal methods.

class Stack:
    stack_1 = list()
    max_length = 10


    def push(self,item):
        self.item = item

        if len(self.stack_1) < self.max_length:
            self.stack_1.append(self.item)
            return self.stack_1

        else:
            return 'stack is full,cant add new item'


    def pop(self):
        if len(self.stack_1) != 0:
            self.stack_1.pop()
            return self.stack_1

        else:
            return "cant pop an empty stack"

    def traversal(self):
        for self.element in self.stack_1:
            print(self.element,end="")
        print('')

        
stk = Stack()
stk.push(6)
# stk.pop()
stk.traversal()
