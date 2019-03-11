# https://www.hackerrank.com/challenges/alternating-characters

def what(arr):
	delete = 0
	for i in range(len(arr)-1):
		cur = arr[i]
		nex = arr[i+1]
		if cur == nex:
			delete+=1
	return delete
