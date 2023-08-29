

def binary_search(arr):
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2
    min_val = 0

    while left < right:

        if arr[mid] < 0

def total_negative(arr):

    # find the total length
    # binary search to find the index where the negative start
    # subtract from the arr len

def count_negative(matrix):

    negative_count = 0

    for arr in matrix:
        negative_count += total_negative(arr)

    print(negative_count)

if __name__ == '__main__':
    matrix = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    count_negative(matrix)