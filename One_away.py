'''
Given two words word1 and word2

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
'''
def isOneAway(string1, string2):
	d= {}
	for i in string1:
		if i not in d:
			d[i] = 1
		else:
			d[i]+=1
	for j in string2:
		if j not in d:
			d[j]=1
		else:
			d[j]-=1
			if d[j]==0:
				del d[j]
	if len(d)==0:
		return True
	elif len(d)==1 and d.values() == [1]:
		return True
	elif len(d)==2 and d.values() == [1, 1]:
		return True
	else:
		return False

print isOneAway("pale", "bake")