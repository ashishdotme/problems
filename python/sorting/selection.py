def selection_sort(arr):
  for i in range(len(arr)):   #[4,3,2,1]
    min = i
    for j in range(i+1,len(arr)):
      if arr[j] < arr[min]:
        min = j
    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp
  return arr

print(selection_sort([3,4,1,2,9,7,8]))