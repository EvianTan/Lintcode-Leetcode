'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '{', '[']
        right  = [')', '}', ']']
        correct = ['()', '{}', '[]']
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                if len(stack) == 0:
                    return False
                hold = stack.pop()
                if hold+i not in correct:
                    return False
        if stack:
            return False
        else:
            return True