'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
Do it in place.
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
	return matrix

matrix = [[1,2,3,4,5],[6,7,8,0,10],[11,0,13,14,15]]
print setZeroes(matrix)