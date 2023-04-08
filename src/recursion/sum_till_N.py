"""
find_total(3)
    |
    --- return 3 + find_total(2)
                   |
                   --- return 2 + find_total(1)
                                  |
                                  --- return 1 + find_total(0)
                                                 |
                                                 --- return 0

"""


def find_total(N: int) -> int:
    """
    Recursively calculates the sum of numbers from 1 to N.

    Args:
    N (int): The upper limit of the sum.

    Returns:
    int: The total sum of numbers from 1 to N.
    """
    if N == 0:
        return 0
    return N + find_total(N - 1)


if __name__ == '__main__':
    total = find_total(3)
    print(total)
