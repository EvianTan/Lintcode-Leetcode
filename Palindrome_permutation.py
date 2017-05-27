'''
Given a string, determine if a permutation of the string could form a palindrome.
For example, input"Tact Coa", output True
'''

def isPalindromePermutation(string):
	A = string.lower()
	D = {}
	for i in A:
		if i != " " and i not in D:
			D[i] = 1
		if i != " " and i in D:
			del D[i]
	return len(D) <= 1

print isPalindromePermutation("Tact Coa")
