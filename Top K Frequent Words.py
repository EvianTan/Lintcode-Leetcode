'''
Given a list of words and an integer k, return the top k frequent words in the list.

 Notice

You should order the words by the frequency of them in the return list, the most frequent one comes first. If two words has the same frequency, the one with lower alphabetical order come first.

Have you met this question in a real interview? Yes
Example
Given

[
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
]
for k = 3, return ["code", "lint", "baby"].

for k = 4, return ["code", "lint", "baby", "yes"],

Challenge 
Do it in O(nlogk) time and O(n) extra space.

Extra points if you can do it in O(n) time with O(k) extra space approximation algorithms.
'''

class Solution:
    """
    @param: words: an array of string
    @param: k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        import heapq
        heap = []
        dict = {}
        for x in words:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
        for key, value in dict.items():
            heapq.heappush(heap, (-value, key))
        res = []
        while heap and k > 0:
            word = heapq.heappop(heap)
            res.append(word[1])
            k -= 1
        return res