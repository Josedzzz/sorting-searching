import time

def measure_time(algorithm, data):
    start = time.time()
    algorithm(data)
    end = time.time()
    return end - start
