# function to sort an array using stooge
def stoogeSort(arr, i, j):
	if arr[i] > arr[j]:
		arr[i], arr[j] = arr[j], arr[i]
	if i + 1 >= j:
		return
	k = (j - i + 1) // 3
	stoogeSort(arr, i, j - k)
	stoogeSort(arr, i + k, j)
	stoogeSort(arr, i, j - k)

