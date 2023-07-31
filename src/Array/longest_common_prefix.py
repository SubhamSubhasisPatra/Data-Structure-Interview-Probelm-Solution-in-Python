def longest_common_prefix(values):
    """
    Find the longest common prefix among a list of strings.

    :param values: The list of strings to find the longest common prefix from.
    :type values: list
    :return: The longest common prefix string.
    :rtype: str
    """
    prefix = ''

    # find the min len element in the array
    min_col_val = min(map(lambda x: len(x), values))

    for index in range(min_col_val):
        ele = values[0][index]
        if all(map(lambda x: x[index] == ele, values)):
            prefix += ele
        else:
            break

    return prefix


if __name__ == '__main__':
    print(longest_common_prefix(['flower', 'flow', 'flight']))
    print(longest_common_prefix(['ab', 'a']))
    print(longest_common_prefix(['cir', 'car']))
