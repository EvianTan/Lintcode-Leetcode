'''
Implement a function to check if a linked list is a palindrome.

Have you met this question in a real interview? Yes
Example
Given 1->2->1, return true

Challenge 
Could you do it in O(n) time and O(1) space?

'''

class solution:
	def isPalindrome(self, head):
		nodes = []
		while head:
			nodes.append(head.val)
			head = head.next
		return nodes == nodes[::-1]
		