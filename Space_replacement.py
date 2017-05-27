
'''
Write a method to replace all spaces in a string with %20. The string is given in a characters array, you can assume it has enough space for replacement and you are given the true length of the string.

You code should also return the new length of the string after replacement.

 Notice

If you are using Java or Python，please use characters array instead of string.

Have you met this question in a real interview? Yes
Example
Given "Mr John Smith", length = 13.

The string after replacement should be "Mr%20John%20Smith", you need to change the string in-place and return the new length 17.

Challenge 
Do it in-place.
'''
class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        if not string:
            return length
    
        space = 0
        for i in string:
            if i == " ":
                space += 1
        L = length + 2*space
        index = L-1
        
        for j in range(length-1, -1, -1):
            if string[j] != " ":
                string[index] = string[j]
                index -= 1
            else:
                string[index] = "0"
                string[index-1] = "2"
                string[index-2] = "%"
                index -= 3