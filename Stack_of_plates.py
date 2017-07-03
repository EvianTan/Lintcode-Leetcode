'''
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. 
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 
Implement a data structure SetOfStacks that mimics this. 
SetOfStacks should be composed of several stacks, and should create a new stack once the previous one exceeds capacity. 
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
'''

class SetOfStacks:
	def __init__(self, capacity):
		self.stacks = []
		if capacity < 1:
			raise NameError("Can't have stacks of that height")
		else:
			self.capacity = capacity

	def push(self, item):
		if self.stacks == []:
			self.stacks.append([item])
		else:
			if len(self.stacks[-1]) >= self.capacity:
				self.stacks.append([item])
			else:
				self.stacks[-1].append(item)

	def pop(self):
		if self.stacks == []:
			raise NameError("can't pop an empty stack")
		else:
			popped_data = self.stacks[-1][-1]
			if len(self.stacks[-1]) == 1:
				del self.stacks[-1]
			else:
				del self.stacks[-1][-1]
			return popped_data