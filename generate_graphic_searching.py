import json
import matplotlib.pyplot as plt

# Load the data from the JSON file
with open("results/search_time.json", "r") as f:
    data = json.load(f)

# Input sizes
sizes = ["10000", "100000", "1000000"]

# Custom colors for each algorithm
colors = {
    "Linear search": "#FF9999",
    "Binary search": "#99CCFF",
    "Ternary search": "#99FF99",
    "Jump search": "#CCCCFF"
}

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

    # Add value labels for all bars
    for bar, time in zip(bars, sorted_times):
        plt.text(time, bar.get_y() + bar.get_height() / 2,
                 f"{time:.8f}s", va='center', ha='left', fontsize=9)

    plt.xscale("log")  # Use logarithmic scale
    plt.xlabel("Execution time (seconds, log scale)")
    plt.title(f"Searching algorithm comparison with {size} elements")
    plt.xlim(1e-6, 1e-1)  # Adjust the X-axis range as needed
    plt.tight_layout()

    # Save and show the plot
    plt.savefig(f"graphics/graph_searching_{size}.png")
    plt.show()

