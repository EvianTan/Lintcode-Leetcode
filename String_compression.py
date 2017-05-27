'''
compress("ddaaaff")
'd2a3f2'
'''

def compress(string):
	res = ''
	count = 1
	res += string[0]
	for i in range(len(string)-1):
		if string[i] == string[i+1]:
			count += 1
		else:
			res += str(count)+string[i+1]
			count = 1

	if string[len(string)-2] == string[len(string)-1]:
		return res+str(count)
	else:
		return res+"1"

print compress("aabcccccaaa")