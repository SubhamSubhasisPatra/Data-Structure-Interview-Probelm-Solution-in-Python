"""
Leetcode -> https://leetcode.com/problems/plus-one/description/
"""


def plus_one(digits):
    """
    Increment a list of digits by 1.

    trick : go from right -> left with the power of 10
    :param digits: A list of digits. Each digit should be an integer from 0 to 9.
    :return: A new list of digits representing the incremented number.

    Example:
        >>> plus_one([1, 2, 3])
        [1, 2, 4]
        >>> plus_one([9, 9, 9])
        [1, 0, 0, 0]

    """
    result = 0
    power = 0
    for index in range(len(digits) - 1, -1, -1):
        result += (digits[index] * (10 ** power))
        power += 1

    result += 1
    return list(map(lambda x: int(x), str(result)))


if __name__ == '__main__':
    output = plus_one([1, 2, 3])
    print(output)
