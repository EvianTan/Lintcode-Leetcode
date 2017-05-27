'''
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Challenge 
Do it in-place.
'''
def rotate(matrix):
        # write your code here
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print matrix
    for i in range(n):
        matrix[i].reverse()
    return matrix

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print rotate(matrix)
