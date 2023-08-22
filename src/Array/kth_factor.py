def kth_factor(number, k):
    """
    Returns the kth factor of the given number.
    Time Complexity O(n/2)

    :param number: The number whose factors we need to find.
    :param k: The position of the factor in the list of factors.
    :return: The kth factor if it exists, -1 otherwise.
    """
    factors = []
    counter = 1
    for i in range(1, (number // 2) + 1):
        if number % i == 0:
            counter += 1
            factors.append(i)

    factors.append(number)

    if counter < k:
        return -1
    return factors[k - 1]


def kth_factor_in_linear(number, k):
    """
    Returns the kth factor of the given number.
    Time Complexity O(n)

    :param number: The number whose factors we need to find.
    :param k: The position of the factor in the list of factors.
    :return: The kth factor if it exists, -1 otherwise.
    """

    for i in range(1, number + 1):
        if number % i == 0:
            k -= 1
            if k == 0:
                return i
    return -1


if __name__ == '__main__':
    print(kth_factor(12, 3))
    print(kth_factor(7, 2))
    print(kth_factor(4, 4))

    print(kth_factor_in_linear(12, 3))
    print(kth_factor_in_linear(7, 2))
    print(kth_factor_in_linear(4, 4))
