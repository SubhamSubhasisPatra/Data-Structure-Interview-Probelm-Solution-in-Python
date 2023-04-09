"""
                              find_subsets(0, [], [3, 1, 2], 3) - 1
                              /                                  \
             find_subsets(1, [3], [3, 1, 2], 3) - 2               find_subsets(1, [], [3, 1, 2], 3) - 3
           /                            \                                /                            \
 find_subsets(2, [3, 1], [3, 1, 2], 3) - 4 find_subsets(2, [3], [3, 1, 2], 3) - 5 find_subsets(2, [1], [3, 1, 2], 3) - 6
           /             \                           /             \                            /             \
find_subsets(3, [3, 1, 2], [3, 1, 2], 3) - 7 find_subsets(3, [3, 2], [3, 1, 2], 3) - 8 find_subsets(3, [1, 2], [3, 1, 2], 3) - 9 find_subsets(3, [2], [3, 1, 2], 3) - 10

Time Complexity -> O(2^n * N )
Space Complexity -> O(N) -> Size of the array || Depth of the tree

"""


def find_subsets(curr_index, curr_subset, arr, length):
    """
    Finds all possible subsets of an array using backtracking and returns them.

    Parameters:
        curr_index (int): Current index of the input array.
        curr_subset (list): Current subset of the input array.
        arr (list): Input array.
        length (int): Length of the input array.

    Returns:
        list: List of all possible subsets of the input array.
    """
    subsets = []

    if curr_index >= length:
        subsets.append(curr_subset[:])
        return subsets

    curr_subset.append(arr[curr_index])
    subsets.extend(find_subsets(curr_index + 1, curr_subset, arr, length))
    curr_subset.pop()
    subsets.extend(find_subsets(curr_index + 1, curr_subset, arr, length))

    return subsets


if __name__ == '__main__':
    input_arr = [ 1, 2,2]
    n = len(input_arr)
    result = find_subsets(0, [], input_arr, n)
    print(result)

