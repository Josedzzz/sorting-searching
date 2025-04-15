import random

# function to generate the files with the data
def generate_file(file_name, amount):
    with open(file_name, 'w') as f:
        for _ in range(amount):
            number = random.randint(10_000_000, 99_999_999)
            f.write(f"{number}\n")

# create the files for the sorting algorithms
generate_file("data/data_sorting_10000.txt", 10000)
generate_file("data/data_sorting_100000.txt", 100000)
generate_file("data/data_sorting_1000000.txt", 1000000)
