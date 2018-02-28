def bubble_sort(arr):
  arr2 = []
  for i in range(len(arr)):
    for j in range(i,len(arr)):
      if arr[i] > arr[j]:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
  return arr

print(bubble_sort([3,4,1,2]))