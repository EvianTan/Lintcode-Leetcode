'''
Given an array of strings, return all groups of strings that are anagrams.

 Notice

All inputs will be in lower-case

Have you met this question in a real interview? Yes
Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

Challenge 
What is Anagram?
- Two strings are anagram if they can be the same after change the order of characters.
'''

class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        dict = {}
        res = []
        for string in strs:
            if  "".join(sorted(string)) not in dict.keys():
                dict["".join(sorted(string))] = 1
            else: 
                dict["".join(sorted(string))] += 1
        for string in strs:
            if dict["".join(sorted(string))] >1:
                res.append(string)
        return res