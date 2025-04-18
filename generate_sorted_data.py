# function to sort a file 
def sort_and_save(input_path, output_path):
    with open(input_path) as f:
        data = list(map(int, f.readlines()))
    data.sort()
    with open(output_path, "w") as f:
        f.writelines(f"{num}\n" for num in data)

sort_and_save("data/data_sorting_10000.txt", "data/data_sorted_10000.txt")
sort_and_save("data/data_sorting_100000.txt", "data/data_sorted_100000.txt")
sort_and_save("data/data_sorting_1000000.txt", "data/data_sorted_1000000.txt")

