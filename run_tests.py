from sortingalgorithms.bitonic_sort import bitonic_sort
from sortingalgorithms.merge_sort import mergeSort
from sortingalgorithms.radix_sort import radixSort
from sortingalgorithms.stooge_sort import stoogeSort
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

# for amount in amounts:
#     print(f"Trying quick sort with {amount} elements...")
#     data = load_data(f"data/data_sorting_{amount}.txt")
#     time = measure_time(lambda arr: quickSort(arr, 0, len(arr) - 1), data.copy())
#     print(f"The execution time is: {time:.4f} seconds")
#     save_results("Quick sort", amount, time)

# for amount in amounts:
#     print(f"\nTrying stooge sort with {amount} elements...")
#     data = load_data(f"data/data_sorting_{amount}.txt")
#     time = measure_time(lambda arr: stoogeSort(arr, 0, len(arr) - 1), data.copy())
#     print(f"The execution time is: {time:.4f} seconds")
#     save_results("Stooge sort", amount, time)

# for amount in amounts:
#     print(f"\nTrying radix sort with {amount} elements...")
#     data = load_data(f"data/data_sorting_{amount}.txt")
#     time = measure_time(radixSort, data.copy())
#     print(f"The execution time is: {time:.4f} seconds")
#     save_results("Radix sort", amount, time)

# for amount in amounts:
#     print(f"\nTrying merge sort with {amount} elements...")
#     data = load_data(f"data/data_sorting_{amount}.txt")
#     time = measure_time(mergeSort, data.copy())
#     print(f"The execution time is: {time:.4f} seconds")
#     save_results("Merge sort", amount, time)

for amount in amounts:
    print(f"\nTrying bitonic sort with {amount} elements...")
    data = load_data(f"data/data_sorting_{amount}.txt")
    # Asegurar que el tamaño del arreglo sea potencia de 2
    length = len(data)
    next_power_of_two = 1 << (length - 1).bit_length()
    if length != next_power_of_two:
        padding = next_power_of_two - length
        print(f"Padding with {padding} zeros to make length {next_power_of_two}")
        data.extend([0] * padding)
    try:
        time = measure_time(bitonic_sort, data.copy())
        print(f"The execution time is: {time:.4f} seconds")
        save_results("Bitonic sort", amount, time)
    except ValueError as e:
        print(f"Skipping {amount} elements: {e}")
