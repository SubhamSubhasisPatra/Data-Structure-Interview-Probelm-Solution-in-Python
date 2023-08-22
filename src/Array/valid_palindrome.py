def valid_palindrome(s):
    """
    Check if a given string is a valid palindrome.

    :param s: The input string to check.
    :return: True if the string is a valid palindrome, False otherwise.

    """
    stack = []

    for ele in s:
        ele = ele.lower()
        if ele.isalnum():
            stack.append(ele)

    return stack == stack[::-1]


if __name__ == '__main__':
    print(valid_palindrome("A man, a plan, a canal: Panama"))
    print(valid_palindrome("race a car"))
    print(valid_palindrome(" "))
    print(valid_palindrome("0P"))
