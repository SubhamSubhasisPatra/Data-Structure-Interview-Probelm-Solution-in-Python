
def remove_duplicates(arr):
    """
    Removes duplicates from an array and returns the count of non-duplicate elements.

    :param arr: The input array from which duplicates will be removed.
    :return: The count of non-duplicate elements in the input array.
    """
    c = 0

    for i in arr:

        if c < 2 or i != arr[c - 2]:
            arr[c] = i
            c += 1
    return c


if __name__ == '__main__':
    numbers = [2, 3, 3, 3, 4, 4, 5]
    remove_duplicates(numbers)
