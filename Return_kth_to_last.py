'''
implement an algorithm to find the kth to last element of a singly linked list
'''

import random 
 
class SinglyLinkedList:
 
    def __init__(self):
        self.head = None
 
    class _Node(object):
        __slots__ = ('_data', '_next')
 
        def __init__(self, data, next):
            self._data = data
            self._next = next
 
    def __iter__(self):
        """makes for nicer printing..."""
        walk = self.head
        while walk is not None:
            yield walk._data
            walk = walk._next
 
    def append(self, data):
        new_node = self._Node(data, self.head)
        self.head = new_node
 
def get_nth_from_end(node, n):
    if node is None:
        return (0, None)
    (i, res) = get_nth_from_end(node._next, n)
    if i == n:
        res = node._data
    i += 1
    return (i, res)
 
l = SinglyLinkedList()
for i in range(10):
    l.append(random.randint(0,20))
 
print('list contents:', list(l))
for i in range(10):
    _, val = get_nth_from_end(l.head, i)
    print('pos {} from last: {}'.format(i, val))
