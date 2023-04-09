"""
                          is_palindrome([1, 2, 3, 2, 1], 0, 5)
                                    /               \
                   True if 1 == 1 /                 \ True if 1 == 1
                   is_palindrome([1, 2, 3, 2, 1], 1, 4)   is_palindrome([1, 2, 3, 2, 1], 1, 4)
                            /               \              /               \
           True if 2 == 2 /                 \ True if 2 == 2 /                 \ True if 2 == 2
           is_palindrome([1, 2, 3, 2, 1], 2, 3)   is_palindrome([1, 2, 3, 2, 1], 2, 3)   is_palindrome([1, 2, 3, 2, 1], 2, 3)
                    |                             |                            |
             True if 3 == 3               True if 3 == 3               True if 3 == 3
           is_palindrome([1, 2, 3, 2, 1], 3, 2)   is_palindrome([1, 2, 3, 2, 1], 3, 2)   is_palindrome([1, 2, 3, 2, 1], 3, 2)
                                                    \                            /
                                                     True if 2 == 2       True if 2 == 2
                                                  is_palindrome([1, 2, 3, 2, 1], 4, 1)
                                                                 |
                                                           True if 1 == 1
                                                         is_palindrome([1, 2, 3, 2, 1], 5, 0)


Note: that the recursion tree has a total of 6 levels, one for each element in the input list. At each level,
the function checks whether the first and last elements of the sub-list are equal, and then recursively checks
the remaining pairs of elements in the sub-list. The base case is reached when there are no more pairs of elements to check,
and the function returns True.
"""


def is_palindrome(data, i, n):
    """
    Check if a given list is a palindrome using recursion.

    :param data: The list to check
    :param i: The start index for the current sub-list
    :param n: The end index for the current sub-list
    :return: True if the sub-list is a palindrome, False otherwise
    """
    # Base case: if we've checked all pairs of elements, the sub-list is a palindrome
    if i >= n // 2:
        return True

    # Check if the first and last elements in the sub-list are equal
    flag = (data[i] == data[n - i - 1])

    # Recursively check the remaining pairs of elements in the sub-list
    return flag and is_palindrome(data, i + 1, n)


if __name__ == '__main__':
    arr = [1, 2, 3, 2, 1]
    f = is_palindrome(arr, 0, 5)
    print(f)
