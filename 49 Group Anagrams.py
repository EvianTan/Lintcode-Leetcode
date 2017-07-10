'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        res = []
        k = 0
        for i in strs:
            hold = ''.join(sorted(i))
            if hold not in dic:
                dic[hold] = k
                k = k+1
                res.append([])
                res[-1].append(i)
            else:
                res[dic[hold]].append(i)
        return res