'''
Binary search is a famous question in algorithm.
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.
If the target number does not exist in the array, return -1.
Example If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.
'''

def binarySearch(array, target):
	if not array:
		return -1
	start, end = 0, len(array) - 1
	while start + 1 < end:
		mid = (start + end) / 2
		if array[mid] == target:
			return mid
		elif array[mid] < target:
			start = mid
		elif array[mid] > target:
			end = mid
	if array[start] == target:
		return start
	if array[end] == target:
		return end
	return -1

array = [1, 2, 3, 3, 4, 5, 10]
target = 3

print binarySearch(array, target)