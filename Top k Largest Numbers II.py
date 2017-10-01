'''
Implement a data structure, provide two interfaces:

add(number). Add a new number in the data structure.
topk(). Return the top k largest numbers in this data structure. k is given when we create the data structure.
Have you met this question in a real interview? Yes
Example
s = new Solution(3);
>> create a new data structure.
s.add(3)
s.add(10)
s.topk()
>> return [10, 3]
s.add(1000)
s.add(-99)
s.topk()
>> return [1000, 10, 3]
s.add(4)
s.topk()
>> return [1000, 10, 4]
s.add(100)
s.topk()
>> return [1000, 100, 10]
'''

import heapq
class Solution:
    # @param {int} k an integer
    def __init__(self, k):
        # initialize your data structure here.
        self.k = k
        self.nums = []
        heapq.heapify(self.nums)

    # @param {int} num an integer
    def add(self, num):
        # Write your code here
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, num)
        elif num > self.nums[0]:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, num)

    # @return {int[]} the top k largest numbers
    def topk(self):
        # Write your code here
        return sorted(self.nums, reverse = True)