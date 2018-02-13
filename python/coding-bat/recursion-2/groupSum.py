def groupSum(index, arr, num):
    if index == len(arr):
        return arr[len(arr) - 1]
    sum = arr[index] + groupSum(index + 1, arr, num)
    if sum == num:
        return True
    else:
        return False


print(groupSum(0, [2, 4, 8], 10))
