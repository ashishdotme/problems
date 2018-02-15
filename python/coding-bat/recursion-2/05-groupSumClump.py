def groupSumClump(index, arr, total):
	if total == 0:
		return True
	if index >= len(arr):
		return total == 0
	return arr

print(groupSumClump(0, [2, 4, 8], 10))