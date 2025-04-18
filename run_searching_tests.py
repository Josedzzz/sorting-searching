from searchingalgorithms.binary_search import binarySearch
from searchingalgorithms.jump_search import jumpSearch
from searchingalgorithms.linear_search import linearSeach
from searchingalgorithms.ternary_search import ternarySearch
from utils.load_data import load_data
from utils.measure_time import measure_searching_time
from utils.save_result import save_results

amounts = [10000, 100000, 1000000]

for amount in amounts:
    print(f"\nRunning linear search with {amount} elements...")
    data = load_data(f"data/data_sorting_{amount}.txt")
    target = data[-1]  # Worst case scenario: last element
    time_taken = measure_searching_time(linearSeach, data, target)
    print(f"Execution time: {time_taken:.6f} seconds")
    save_results("Linear search", amount, time_taken, "results/search_time.json")

for amount in amounts:
    print(f"\nRunning binary search with {amount} elements...")
    data = load_data(f"data/data_sorting_{amount}.txt")
    target = data[-1]  # Worst case scenario: last element
    time_taken = measure_searching_time(binarySearch, data, target)
    print(f"Execution time: {time_taken:.6f} seconds")
    save_results("Binary search", amount, time_taken, "results/search_time.json")

for amount in amounts:
    print(f"\nRunning ternary search with {amount} elements...")
    data = load_data(f"data/data_sorting_{amount}.txt")
    target = data[-1]  # Worst case scenario: last element
    time_taken = measure_searching_time(ternarySearch, data, target)
    print(f"Execution time: {time_taken:.6f} seconds")
    save_results("Ternary search", amount, time_taken, "results/search_time.json")


for amount in amounts:
    print(f"\nRunning jump search with {amount} elements...")
    data = load_data(f"data/data_sorting_{amount}.txt")
    target = data[-1]  # Worst case scenario: last element
    time_taken = measure_searching_time(jumpSearch, data, target)
    print(f"Execution time: {time_taken:.6f} seconds")
    save_results("Jump search", amount, time_taken, "results/search_time.json")
