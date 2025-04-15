from sortingalgorithms.quick_sort import quickSort
from utils.load_data import load_data
from utils.measure_time import measure_time
from sortingalgorithms.bubble_sort import bubble_sort
from utils.save_result import save_results

amounts = [10000, 100000, 1000000]

# for amount in amounts:
#     print(f"Trying bubble sort with {amount} elements...")
#     data = load_data(f"data/data_sorting_{amount}.txt")
#     time = measure_time(bubble_sort, data.copy())
#     print(f"The execution time is: {time:.4f} seconds")
#
#     save_results("Bubble sort", amount, time)

for amount in amounts:
    print(f"Trying quick sort with {amount} elements...")
    data = load_data(f"data/data_sorting_{amount}.txt")
    time = measure_time(lambda arr: quickSort(arr, 0, len(arr) - 1), data.copy())
    print(f"The execution time is: {time:.4f} seconds")
    save_results("Quick sort", amount, time)
