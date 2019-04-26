def BinarySearch(lists, item):
	'''
	lists must be sorted
	'''
	low = 0
	high = len(lists) - 1
	while low <= high:
		mid = (low + high) // 2
		guess = lists[mid]
		if guess == item:
			return item
		if guess > item:
			high = mid -1
		else:
			low = mid +1
	return None

myList = [1,3,5,7,9,10,13]

result = BinarySearch(myList, 5)
print(result)
