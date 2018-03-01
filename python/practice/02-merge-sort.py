def merge(arr, l, m, r):
    print(arr[l:r])


def mergeSort(arr, l, r):
    if l < r:
        mid = l + (r - l) / 2
        mergeSort(arr, l, int(mid))
        mergeSort(arr, int(mid) + 1, r)
        merge(arr, l, int(mid), r)


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print(mergeSort(arr, 0, n - 1))
