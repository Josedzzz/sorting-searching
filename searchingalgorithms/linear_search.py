# function to do a linear search
def linearSeach(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

