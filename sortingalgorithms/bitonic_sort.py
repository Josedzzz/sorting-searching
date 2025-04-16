# Bitonic Sort implementation

ASCENDING = True
DESCENDING = False

def compare_and_swap(arr, i, j, direction):
    if (direction == ASCENDING and arr[i] > arr[j]) or (direction == DESCENDING and arr[i] < arr[j]):
        arr[i], arr[j] = arr[j], arr[i]

def bitonic_merge(arr, low, cnt, direction):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            compare_and_swap(arr, i, i + k, direction)
        bitonic_merge(arr, low, k, direction)
        bitonic_merge(arr, low + k, k, direction)

def bitonic_sort_recursive(arr, low, cnt, direction):
    if cnt > 1:
        k = cnt // 2
        bitonic_sort_recursive(arr, low, k, ASCENDING)
        bitonic_sort_recursive(arr, low + k, k, DESCENDING)
        bitonic_merge(arr, low, cnt, direction)

def bitonic_sort(arr):
    n = len(arr)
    if (n & (n - 1)) != 0:
        raise ValueError("Bitonic sort requires array length to be a power of 2.")
    bitonic_sort_recursive(arr, 0, n, ASCENDING)

