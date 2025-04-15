import json
import os

# save the results on a json
def save_results(algorithm_name, amount, time, path = "results/time.json"):
    results = {}
    if os.path.exists(path):
        with open(path, "r") as f:
            results = json.load(f)
    if algorithm_name not in results:
        results[algorithm_name] = {}
    results[algorithm_name][str(amount)] = time
    with open(path, "w") as f:
        json.dump(results, f, indent=4)

