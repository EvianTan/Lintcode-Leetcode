'''
Implement a stack with min() function, which will return the smallest number in the stack.

It should support push, pop and min operation all in O(1) cost.

Example
push(1)
pop()   // return 1
push(2)
push(3)
min()   // return 2
push(1)
min()   // return 1
'''

class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.minstack = []

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if len(self.minstack) == 0 or number <= self.minstack[-1]:
            self.minstack.append(number)

    def pop(self):
        # pop and return the top item in stack
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()

    def min(self):
        # return the minimum number in stack
        return self.minstack[-1]