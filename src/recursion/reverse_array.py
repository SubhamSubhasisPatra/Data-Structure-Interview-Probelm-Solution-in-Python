"""
reverse(['a', 'b', 'c'], 0, 2)
             /      |      \
        swap a & c   |      return ['c', 'b', 'a']
                   swap b & b

"""


def single_var_swap(data, i, n):
    """
    :description Single variable
    :param data:
    :param i:
    :param n:
    :return:
    """
    if i >= n // 2:
        return data
    data[i], data[n - i - 1] = data[n - i - 1], data[i]
    return single_var_swap(data, i + 1, n)


def reverse(data, start, end):
    """
    :description Two pointer approach
    :param data:
    :param start:
    :param end:
    :return:
    """
    if start >= end:
        return data
    data[start], data[end] = data[end], data[start]
    return reverse(data, start + 1, end - 1)


if __name__ == '__main__':
    arr = reverse(['a', 'b', 'c'], 0, 2)
    print(arr)
    print()
    new_arr = single_var_swap(['a', 'b', 'c'], 0, 3)
    print(new_arr)
