# function to load the data given a path
def load_data(path):
    with open(path, 'r') as f:
        return [int(line.strip()) for line in f]

