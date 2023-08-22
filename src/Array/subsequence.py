def is_subsequence(s, t):
    """
    Check if a string s is a subsequence of string t.

    :param s: The string to be checked for subsequence.
    :param t: The string in which to search for the subsequence.
    :return: True if s is a subsequence of t, False otherwise.
    """
    i, j = 0, 0

    while j < len(t):

        if i < len(s) and s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


if __name__ == '__main__':
    s = 'abc'
    t = 'axybvzc'
    print(is_subsequence(s, t))
