'''
Given a string which contains only letters. Sort it by lower case first and upper case second.

 Notice

It's NOT necessary to keep the original order of lower-case letters and upper case letters.

Have you met this question in a real interview? Yes
Example
For "abAcD", a reasonable answer is "acbAD"

Challenge 
Do it in one-pass and in-place.
'''

class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here
        if len(chars) <= 1:
            return
        i = 0
        j = len(chars)-1
        while i < j:
            while i < len(chars)-1 and chars[i] in 'abcdefghijklmnopqrstuvwxyz':
                i += 1
            while j > 0 and chars[j] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                j -= 1
            while i<j and chars[i] not in 'abcdefghijklmnopqrstuvwxyz' and chars[j] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                temp = chars[i]
                chars[i] = chars[j]
                chars[j] = temp
                i += 1
                j -= 1