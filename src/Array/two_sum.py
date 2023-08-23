def sorted_two_sum(arr, target):
    """
    :param arr: List of integers in ascending order.
    :param target: Target sum.
    :return: List of two indices that sum up to the target sum, if found. Otherwise, returns None.

    This method takes a sorted list of integers and a target sum as input. It finds two elements in the list that sum up to the target sum. The method returns a list of two indices, representing the positions of the two elements in the original list. If no such pair is found, it returns None.

    Example:
        arr = [1, 2, 3, 4, 5]
        target = 7
        sorted_two_sum(arr, target) => [2, 4]

    Note:
        - The input list must be sorted in ascending order for this method to work correctly.
        - The returned indices are 1-based, indicating the positions of the elements in the original list.
    """
    reverse_mapping = {}

    for index, value in enumerate(arr):
        if target - value in reverse_mapping:
            return [reverse_mapping[target - value] + 1, index + 1]
        reverse_mapping[value] = index


def two_pointer(arr, target):
    """
    :param arr: A list of integers representing the input array.
    :param target: An integer representing the target sum.
    :return: A list of two integers representing the indices of the two elements in the input array that sum up to the target. If no such pair is found, returns None.

    The `two_pointer` method takes an input array `arr` and a target sum `target`. It initializes two pointers, `left` and `right`, to point to the first and last elements of the array, respectively. It then iteratively compares the sum of the numbers at the `left` and `right` indices with the target sum. If the sum is equal to the target, it returns the indices in a list. If the sum is less than the target, it increments the `left` pointer to move to the next element. If the sum is greater than the target, it decrements the `right` pointer to move to the previous element.

    Example Usage:
    arr = [2, 7, 11, 15]
    target = 9
    result = two_pointer(arr, target)
    print(result)  # Output: [1, 2]
    """
    left, right = 0, len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1


if __name__ == '__main__':
    arr1, target1 = [2, 7, 11, 15], 9
    print(sorted_two_sum(arr1, target1))
    print(two_pointer(arr1, target1))
