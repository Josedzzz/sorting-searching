import time

def measure_time(algorithm, data):
    start = time.time()
    algorithm(data)
    end = time.time()
    return end - start

def measure_searching_time(algorithm, arr, target):
    start = time.time()
    algorithm(arr, target)
    end = time.time()
    return end - start
