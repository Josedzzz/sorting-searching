import json
import matplotlib.pyplot as plt

# Load the data from the JSON file
with open("results/time.json", "r") as f:
    data = json.load(f)

# Input sizes
sizes = ["10000", "100000", "1000000"]

# Custom colors for each algorithm
colors = {
    "Bubble sort": "#FF9999",
    "Quick sort": "#99CCFF",
    "Stooge sort": "#FFCC99",
    "Radix sort": "#99FF99",
    "Merge sort": "#CCCCFF",
    "Bitonic sort": "#FFB6C1"
}

# Maximum time to display on the X-axis (adjust as needed)
time_limit = 20

for size in sizes:
    plt.figure(figsize=(10, 6))
    algos = []
    times = []

    for algo, results in data.items():
        if size in results:
            algos.append(algo)
            times.append(results[size])

    # Sort by execution time
    sorted_pairs = sorted(zip(times, algos))
    sorted_times, sorted_algos = zip(*sorted_pairs)

    # Set bar colors
    bar_colors = [colors.get(algo, "#cccccc") for algo in sorted_algos]

    # Draw horizontal bar chart
    bars = plt.barh(sorted_algos, sorted_times, color=bar_colors)

    # Add labels for bars that exceed the time limit
    for bar, time in zip(bars, sorted_times):
        if time > time_limit:
            plt.text(time_limit, bar.get_y() + bar.get_height() / 2,
                     f"{time:.1f}s →", va='center', ha='left', color="red", fontsize=10)

    plt.xlabel("Execution time (seconds)")
    plt.title(f"Algorithm comparison with {size} elements")
    plt.xlim(0, time_limit)  # Limit X-axis range
    plt.tight_layout()

    # Save and show the plot
    plt.savefig(f"graphics/graph_sorting_{size}.png")
    plt.show()

