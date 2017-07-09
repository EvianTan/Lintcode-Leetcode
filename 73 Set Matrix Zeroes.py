'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

def setZeroes(matrix):
	if len(matrix)==0:
		return
	n = len(matrix)
	m = len(matrix[0])
	row = [False for i in range(n)]
	col = [False for i in range(m)]
	for i in range(n):
		for j in range(m):
			if matrix[i][j] == 0:
				row[i] = True
				col[j] = True
	for i in range(n):
		for j in range(m):
			if row[i] or col[j]:
				matrix[i][j] = 0